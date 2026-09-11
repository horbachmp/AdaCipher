import os
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from models.base_model import Model


transformers.logging.set_verbosity_error()


class QwenModel(Model):
    def __init__(
        self,
        model_name: str = "Qwen/Qwen3.5-27B",
        max_new_tokens: int = 512,
        devices: list = [1,2,3],
        cache_dir: str = None,
        local_model_dir: str = None,
        seed: int = 0,
        temperature: float = 0.0
    ):
        super().__init__(model_name, max_new_tokens, seed, temperature)

        torch.manual_seed(seed)

        if devices is None:
            devices = []
        self.devices = devices if isinstance(devices, list) else [devices]

        model_source = local_model_dir if local_model_dir and os.path.isdir(local_model_dir) else model_name
        local_files_only = bool(local_model_dir and os.path.isdir(local_model_dir))

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_source,
            cache_dir=cache_dir,
            local_files_only=local_files_only,
            trust_remote_code=True,
        )

        # Determine device mapping for multi-GPU support
        if len(self.devices) > 1:
            # Multiple GPUs: use auto device_map
            device_map = "auto"
        elif len(self.devices) == 1:
            # Single GPU
            device = self.devices[0]
            if isinstance(device, int):
                device_map = f"cuda:{device}"
            else:
                device_map = device
        else:
            # CPU
            device_map = "cpu"

        self.model = AutoModelForCausalLM.from_pretrained(
            model_source,
            device_map=device_map,
            dtype=torch.bfloat16,
            cache_dir=cache_dir,
            local_files_only=local_files_only,
            trust_remote_code=True,
        )

        if local_model_dir and not os.path.isdir(local_model_dir):
            os.makedirs(local_model_dir, exist_ok=True)
            self.tokenizer.save_pretrained(local_model_dir)
            self.model.save_pretrained(local_model_dir)

        self.max_new_tokens = max_new_tokens

        # Set device for input processing
        if len(self.devices) > 0:
            # For multi-GPU, use first device for input processing
            first_device = self.devices[-1]
            if isinstance(first_device, int):
                self.device = f"cuda:{first_device}"
            else:
                self.device = first_device
        else:
            self.device = "cpu"

    def ask(self, question: str, system_prompt: str = None, few_shot: list = None) -> str:
        if few_shot is None:
            few_shot = []

        messages = [
            {"role": "system", "content": system_prompt},
            *few_shot,
            {"role": "user", "content": question},
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=False,
            enable_thinking=False,
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)

        print(f"Input tokens: {inputs['input_ids'].shape[-1]}")

        with torch.no_grad():
            torch.cuda.empty_cache()
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                do_sample=False,
            )

        generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
        response = self.tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()

        return response
