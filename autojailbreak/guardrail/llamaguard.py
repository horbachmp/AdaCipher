# guardrail_pipeline.py

from typing import Optional, List, Dict
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from guardrail.guard_decision import GuardDecision


CONTENT_FLAG = "content"
ROLE_FLAG = "role"

# Accelerate gets slightly less than the full card so model loading has room
# for its own transient buffers.
GPU_MEMORY_FRACTION = 0.98

# Smallest padding block worth allocating while filling up a GPU.
MIN_RESERVE_BLOCK = 64 * 1024 ** 2


class GuardOutOfMemoryError(RuntimeError):
    """Raised when moderation fails because the GPU ran out of memory."""


CATEGORY_NAMES = {
    "S1": "violent crimes",
    "S2": "non-violent crimes",
    "S3": "sex-related crimes",
    "S4": "child sexual exploitation",
    "S5": "defamation",
    "S6": "specialized advice",
    "S7": "privacy",
    "S8": "intellectual property",
    "S9": "indiscriminate weapons",
    "S10": "hate",
    "S11": "suicide & self-harm",
    "S12": "sexual content",
    "S13": "elections",
    "S14": "code interpreter abuse",
}


class LocalLlamaGuard:
    """
    Local Hugging Face wrapper for Llama Guard-style moderation.

    This version does NOT change the model prompt.
    It only parses the model output into:
      - allowed
      - category
      - reason
      - raw
    """

    def __init__(
        self,
        model_id: str = "meta-llama/Llama-Guard-3-8B",
        devices: Optional[List] = None,
        torch_dtype: Optional[torch.dtype] = torch.bfloat16,
        max_new_tokens: int = 64,
        max_memory_per_gpu: Optional[str] = None,
        max_memory_cpu: str = "30GB",
        reserve_full_gpu_memory: bool = True,
        reserve_headroom: str = "1GB",
    ):
        """
        reserve_full_gpu_memory: claim the free memory of `devices` for this
            process (see _reserve_gpu_memory). The claim is reusable by this
            process, so it costs nothing at inference time.
        reserve_headroom: how much to leave unclaimed on each card — room for
            the allocator's small pool and CUDA's own allocations, not the
            inference budget.
        """
        self.model_id = model_id
        self.max_new_tokens = max_new_tokens
        self._reserved_bytes: Dict[int, int] = {}

        if devices is None:
            devices = []
        self.devices = devices if isinstance(devices, list) else [devices]

        self.tokenizer = AutoTokenizer.from_pretrained(model_id)

        load_kwargs = {
            "device_map": self._build_device_map(),
            "torch_dtype": torch_dtype,
        }
        max_memory = self._build_max_memory(max_memory_per_gpu, max_memory_cpu)
        if max_memory:
            load_kwargs["max_memory"] = max_memory

        self.model = AutoModelForCausalLM.from_pretrained(model_id, **load_kwargs)
        self.model.eval()

        if reserve_full_gpu_memory:
            self._reserve_gpu_memory(self._parse_size(reserve_headroom))

    @staticmethod
    def _parse_size(size: str) -> int:
        """Convert a '45GB' / '512MB' style string to bytes."""
        match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*([KMGT]?)i?B?\s*", str(size), re.IGNORECASE)
        if not match:
            raise ValueError(f"unparseable memory size: {size!r}")
        units = {"": 1, "K": 1024, "M": 1024 ** 2, "G": 1024 ** 3, "T": 1024 ** 4}
        return int(float(match.group(1)) * units[match.group(2).upper()])

    def _device_indices(self) -> List[int]:
        """CUDA indices of the configured devices (empty when running on CPU)."""
        indices = []
        for device in self.devices:
            if isinstance(device, int):
                indices.append(device)
                continue
            text = str(device)
            if text.startswith("cuda"):
                indices.append(int(text.split(":")[-1]) if ":" in text else 0)
            elif text.isdigit():
                indices.append(int(text))
        return indices

    @staticmethod
    def _is_oom(exc: BaseException) -> bool:
        return isinstance(exc, torch.cuda.OutOfMemoryError) or (
            isinstance(exc, RuntimeError) and "CUDA out of memory" in str(exc)
        )

    @classmethod
    def _allocate_block(cls, index: int, size: int) -> Optional[torch.Tensor]:
        """
        Grab `size` bytes on the GPU in one piece, halving the request on OOM
        until it fits or drops below MIN_RESERVE_BLOCK. One large block is
        both faster and less fragmenting than many small ones.
        """
        while size >= MIN_RESERVE_BLOCK:
            try:
                return torch.empty(size, dtype=torch.uint8, device=f"cuda:{index}")
            except Exception as exc:
                if not cls._is_oom(exc):
                    raise
                size //= 2
        return None

    def _reserve_gpu_memory(self, headroom_bytes: int) -> None:
        """
        Claim the free memory of the configured GPUs for this process, while
        keeping it available to this process.

        The padding blocks are allocated and then dropped straight away. Freeing
        the tensor does not return the memory to the driver: the PyTorch caching
        allocator keeps the segment, so the card still looks fully occupied to
        every other process (nvidia-smi included) and nobody can start a job on
        it — but our own allocations are served from that cache instead of asking
        the driver for more. The memory is therefore reserved *and* usable.

        The only thing that hands it back is torch.cuda.empty_cache() (ours, in
        release_reserved_memory, or one from another library).

        `headroom_bytes` is what is deliberately left unclaimed on each card.
        It is not the inference budget — inference reuses the whole reservation
        — but it must stay non-zero: the caching allocator serves allocations
        below 1MB from a separate small pool that cannot reuse these large
        segments, and CUDA itself needs room for context-level allocations.
        """
        if not torch.cuda.is_available():
            return

        for index in self._device_indices():
            with torch.cuda.device(index):
                blocks: List[torch.Tensor] = []
                while True:
                    free, _ = torch.cuda.mem_get_info()
                    size = free - headroom_bytes
                    if size <= 0:
                        break
                    block = self._allocate_block(index, size)
                    if block is None:
                        break
                    blocks.append(block)

                claimed = sum(block.numel() for block in blocks)
                # hand the blocks to the caching allocator: still ours, now reusable
                blocks.clear()
                torch.cuda.synchronize()
                self._reserved_bytes[index] = claimed
                print(
                    f"[Guard] Reserved {claimed / 1024 ** 3:.2f} GiB on cuda:{index} "
                    f"(cached for reuse by this process)"
                )

    def release_reserved_memory(self) -> None:
        """Give the reserved GPU memory back (frees it for other processes)."""
        self._reserved_bytes.clear()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    def _build_device_map(self):
        """
        Multiple devices: shard the model across them ("auto" + max_memory).
        One device: place the whole model on it.
        No devices: CPU.
        """
        if len(self.devices) > 1:
            return "auto"

        if len(self.devices) == 1:
            device = self.devices[0]
            return f"cuda:{device}" if isinstance(device, int) else device

        return "cpu"

    def _build_max_memory(
        self, max_memory_per_gpu: Optional[str], max_memory_cpu: str
    ) -> Optional[Dict]:
        """
        Restrict sharding to the configured devices only: accelerate places
        weights exclusively on the keys listed here.

        Without an explicit per-GPU budget each GPU is given its full
        capacity, so accelerate is free to use the whole card.
        """
        if len(self.devices) <= 1:
            return None

        max_memory = {}
        for index in self._device_indices():
            if max_memory_per_gpu is None:
                total = torch.cuda.get_device_properties(index).total_memory
                max_memory[index] = int(total * GPU_MEMORY_FRACTION)
            else:
                max_memory[index] = max_memory_per_gpu
        max_memory["cpu"] = max_memory_cpu
        return max_memory

    def _format_messages(self, messages: List[Dict[str, str]]) -> str:
        """
        Convert messages to model input using the tokenizer chat template.
        The prompt content itself is not modified.
        """
        if hasattr(self.tokenizer, "apply_chat_template"):
            return self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )

        text = ""
        for m in messages:
            role = m["role"].upper()
            text += f"{role}: {m['content']}\n"
        text += "ASSISTANT:"
        return text

    def _generate(self, messages: List[Dict[str, str]]) -> str:
        prompt_text = self._format_messages(messages)

        inputs = self.tokenizer(
            prompt_text,
            return_tensors="pt",
        ).to(self.model.device)

        try:
            with torch.no_grad():
                output = self.model.generate(
                    **inputs,
                    max_new_tokens=self.max_new_tokens,
                    do_sample=False,
                    temperature=0.0,
                )
        except Exception as exc:
            if not self._is_oom(exc):
                raise
            raise GuardOutOfMemoryError(
                "GPU out of memory during moderation. The reservation is reusable, so this "
                "is a genuine shortage: lower the number of guard calls running at once "
                "(max_concurrency in the attack loop), shorten the prompt, or lower "
                "max_new_tokens"
            ) from exc

        gen_tokens = output[0][inputs["input_ids"].shape[-1]:]
        raw = self.tokenizer.decode(gen_tokens, skip_special_tokens=True)
        return raw.strip()

    @staticmethod
    def _parse_categories(raw: str) -> Optional[List[str]]:
        """
        Parse categories from the second non-empty line, e.g.:
          unsafe
          S1
        or
          unsafe
          S1,S2
        """
        if not raw:
            return None

        lines = [line.strip() for line in raw.splitlines() if line.strip()]
        if len(lines) < 2:
            return None

        cat_line = lines[1].strip()
        cats = [c.strip().upper() for c in re.split(r"[,\s]+", cat_line) if c.strip()]
        cats = [c for c in cats if re.fullmatch(r"S\d+", c)]

        if not cats:
            return None

        seen = set()
        deduped = []
        for c in cats:
            if c not in seen:
                seen.add(c)
                deduped.append(c)

        return deduped

    @staticmethod
    def _format_categories(categories: Optional[List[str]]) -> Optional[str]:
        if not categories:
            return None
        return ",".join(categories)

    @staticmethod
    def _reason_from_categories(categories: Optional[List[str]], allowed: bool) -> Optional[str]:
        if allowed:
            return "benign content"

        if not categories:
            return "unsafe content"

        if "S1" in categories:
            return "violent crimes"
        if "S2" in categories:
            return "non-violent crimes"
        if "S3" in categories:
            return "sex-related crimes"
        if "S4" in categories:
            return "child sexual exploitation"
        if "S5" in categories:
            return "defamation"
        if "S6" in categories:
            return "specialized advice"
        if "S7" in categories:
            return "privacy"
        if "S8" in categories:
            return "intellectual property"
        if "S9" in categories:
            return "indiscriminate weapons"
        if "S10" in categories:
            return "hate"
        if "S11" in categories:
            return "suicide & self-harm"
        if "S12" in categories:
            return "sexual content"
        if "S13" in categories:
            return "elections"
        if "S14" in categories:
            return "code interpreter abuse"

        return "unsafe content"

    def check(self, messages: List[Dict[str, str]]) -> GuardDecision:
        raw = self._generate(messages)
        parsed = raw.strip().lower()

        if parsed.startswith("safe"):
            return GuardDecision(
                allowed=True,
                category=None,
                reason="benign content",
                raw=raw,
            )

        if parsed.startswith("unsafe"):
            categories = self._parse_categories(raw)
            category_str = self._format_categories(categories) or "unknown"
            reason = self._reason_from_categories(categories, allowed=False)
            return GuardDecision(
                allowed=False,
                category=category_str,
                reason=reason,
                raw=raw,
            )

        return GuardDecision(
            allowed=False,
            category="unknown",
            reason="unparseable response",
            raw=raw,
        )

    def check_input(
        self,
        user_text: str,
        system_prompt: Optional[str] = None,
        few_shot: Optional[List[Dict[str, str]]] = None,
    ) -> GuardDecision:
        messages: List[Dict[str, str]] = []

        if few_shot:
            messages.extend(few_shot)

        user_content = user_text
        if system_prompt:
            user_content = f"{system_prompt}\n{user_text}"

        messages.append({"role": "user", "content": user_content})
        return self.check(messages)

    def check_output(
        self,
        user_text: str,
        assistant_text: str,
        system_prompt: Optional[str] = None,
        few_shot: Optional[List[Dict[str, str]]] = None,
    ) -> GuardDecision:
        messages: List[Dict[str, str]] = []

        if few_shot:
            messages.extend(few_shot)

        user_content = user_text
        if system_prompt:
            user_content = f"{system_prompt}\n{user_text}"

        messages.append({"role": "user", "content": user_content})
        messages.append({"role": "assistant", "content": assistant_text})
        return self.check(messages)
