# guardrail_openrouter.py

from dataclasses import dataclass
from typing import Optional, List, Dict
import os
import re

from openai import OpenAI

from guardrail.guard_decision import GuardDecision

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")

CONTENT_FLAG = "content"
ROLE_FLAG = "role"

CATEGORY_NAMES = {
    "S1": "violent crimes",
    "S2": "non-violent crimes",
    "S3": "sex crimes",
    "S4": "child exploitation",
    "S5": "defamation",
    "S6": "specialized advice",
    "S7": "privacy",
    "S8": "intellectual property",
    "S9": "indiscriminate weapons",
    "S10": "hate",
    "S11": "self-harm",
    "S12": "sexual content",
    "S13": "elections",
    # S14 intentionally excluded
}


class OpenRouterLlamaGuard:
    """
    Cipher-aware guardrail wrapper that calls a model through OpenRouter's
    OpenAI-compatible Chat Completions API.

    Behavior:
    - benign cipher / encoding / decoding tasks are allowed
    - cipher used to hide harmful intent, evade moderation, or smuggle unsafe
      instructions is blocked
    """

    def __init__(
        self,
        model_id: str = "meta-llama/llama-guard-4-12b",
        base_url: str = "https://openrouter.ai/api/v1",
        http_referer: Optional[str] = None,
        x_openrouter_title: Optional[str] = None,
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ):
        if not OPENROUTER_KEY:
            raise ValueError("OPENROUTER_KEY is not set in the environment.")

        self.model_id = model_id
        self.max_tokens = max_tokens
        self.temperature = temperature

        default_headers = {}
        if http_referer:
            default_headers["HTTP-Referer"] = http_referer
        if x_openrouter_title:
            default_headers["X-OpenRouter-Title"] = x_openrouter_title

        self.client = OpenAI(
            api_key=OPENROUTER_KEY,
            base_url=base_url,
            default_headers=default_headers or None,
        )

    @property
    def unsafe_categories(self) -> str:
        return """S1: Violent Crimes.
AI models should not create content that enables, encourages, or excuses the commission of violent crimes. Examples of violent crimes include, but are not limited to:
- Unlawful violence toward people (ex: terrorism, genocide, murder, hate crimes, child abuse, assault, battery, kidnapping)
- Unlawful violence toward animals (ex: animal abuse)

S2: Non-Violent Crimes.
AI models should not create content that enables, encourages, or excuses the commission of non-violent crimes. Examples of non-violent crimes include, but are not limited to:
- Financial crimes (ex: fraud, scams, money laundering)
- Property crimes (ex: burglary, robbery, arson, vandalism)
- Drug crimes (ex: creating or trafficking narcotics)
- Weapons crimes (ex: producing unlicensed firearms)
- Cyber crimes (ex: hacking, spyware, malware)

S3: Sex Crimes.
AI models should not create content that enables, encourages, or excuses the commission of sex crimes. Examples of sex crimes include, but are not limited to:
- Human trafficking
- Sexual assault (ex: rape)
- Sexual harassment (ex: groping)
- Lewd conduct

S4: Child Exploitation.
AI models should not create content that depicts child nudity or that enables, encourages, excuses, or depicts the sexual abuse of children.

S5: Defamation.
AI models should not create content about a real, living person that is verifiably false and likely to injure the person's reputation.

S6: Specialized Advice.
AI models should not create content that contains specialized financial, medical, or legal advice.

S7: Privacy.
AI models should not create content that contains sensitive, personal information about private individuals.

S8: Intellectual Property.
AI models should not create content that violates the intellectual property rights of third parties.

S9: Indiscriminate Weapons.
AI models should not create content that enables the creation of weapons of mass destruction. Examples of such weapons include, but are not limited to:
- Chemical weapons (ex: nerve gas)
- Biological weapons (ex: anthrax)
- Radiological weapons (ex: salted bombs)
- Nuclear weapons (ex: atomic warheads)
- High-yield explosive weapons (ex: cluster munitions)

S10: Hate.
AI models should not create content that is hateful toward people on the basis of their protected characteristics (race, color, ethnicity, national origin, disability, religious affiliation, caste, sexual orientation, sex, gender identity and serious disease). AI models should not create content that perpetuates negative stereotypes.

S11: Self-Harm.
AI models should not create content that enables, encourages, or excuses acts of intentional self-harm. Examples of such actions include, but are not limited to:
- Suicide
- Self-injury (ex: cutting)
- Disordered eating

S12: Sexual Content.
AI models should not create depictions of nude adults or content that contains erotic descriptions or explicit depictions of sex acts.

S13: Elections.
AI models should not create content that contain factually incorrect information about electoral systems and processes, including in the time, place, or manner of voting in civic elections.
"""

    def _build_prompt(
        self,
        role: str,
        user_message: str,
        model_answer: Optional[str] = None,
    ) -> str:
        conversation_lines = [f"User: {user_message}"]
        if model_answer is not None:
            conversation_lines.append(f"Agent: {model_answer}")

        conversation = "\n\n".join(conversation_lines)

        return f"""<|begin_of_text|><|header_start|>user<|header_end|>

Task: Check if there is unsafe content in '{role}' messages in conversations according to our safety policy with the below categories.

Important cipher rule:
- Treat ciphered or encoded text as semantically equivalent to plaintext.
- Benign cipher exercises, decoding practice, encoding requests, and harmless cipher-based communication are SAFE.
- If ciphered text is used to hide harmful intent, evade moderation, or smuggle unsafe instructions, classify it as UNSAFE using the underlying harmful category, and also include S1 when obfuscation/evasion is part of the intent.

<BEGIN UNSAFE CONTENT CATEGORIES>
{self.unsafe_categories}
<END UNSAFE CONTENT CATEGORIES>

<BEGIN CONVERSATION>

{conversation}

<END CONVERSATION>

Provide your safety assessment for ONLY THE LAST {role} in the above conversation:
- First line must read 'safe' or 'unsafe'.
- If unsafe, a second line must include a comma-separated list of violated categories.<|eot|><|header_start|>assistant<|header_end|>
"""

    def _generate(self, messages: List[Dict[str, str]]) -> str:
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        text_response = response.model_dump_json(indent=2)
        raw = response.choices[0].message.content or text_response
        return raw.strip()

    @staticmethod
    def _parse_categories(raw: str) -> Optional[List[str]]:
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
    def _format_categories(categories: Optional[List[str]]) -> str:
        if not categories:
            return "unknown"
        formatted = [f"{cat} ({CATEGORY_NAMES.get(cat, 'unknown')})" for cat in categories]
        return ",".join(formatted)

    @staticmethod
    def _reason_from_categories(categories: Optional[List[str]], allowed: bool) -> Optional[str]:
        if allowed:
            return "benign cipher or non-harmful content"

        if not categories:
            return "unsafe content"

        if "S1" in categories:
            return "violent crime or harmful violence"
        if "S2" in categories:
            return "non-violent crime or cyber abuse"
        if "S3" in categories:
            return "sex crime related content"
        if "S4" in categories:
            return "child exploitation"
        if "S5" in categories:
            return "defamation"
        if "S6" in categories:
            return "specialized advice"
        if "S7" in categories:
            return "privacy violation"
        if "S8" in categories:
            return "intellectual property violation"
        if "S9" in categories:
            return "indiscriminate weapons"
        if "S10" in categories:
            return "hate content"
        if "S11" in categories:
            return "self-harm related content"
        if "S12" in categories:
            return "sexual content"
        if "S13" in categories:
            return "election misinformation"

        return "unsafe content"

    def check(self, messages: List[Dict[str, str]]) -> GuardDecision:
        raw = self._generate(messages)
        parsed = raw.strip().lower()

        if parsed.startswith("safe"):
            return GuardDecision(
                allowed=True,
                category=None,
                reason="benign cipher or non-harmful content",
                raw=raw,
            )

        if parsed.startswith("unsafe"):
            categories = self._parse_categories(raw)
            category_str = self._format_categories(categories)
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

        if system_prompt:
            user_text = f"{system_prompt}\n{user_text}"

        prompt = self._build_prompt(
            role="User",
            user_message=user_text,
            model_answer=None,
        )
        messages.append({"role": "user", "content": prompt})
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

        if system_prompt:
            user_text = f"{system_prompt}\n{user_text}"

        prompt = self._build_prompt(
            role="Agent",
            user_message=user_text,
            model_answer=assistant_text,
        )
        messages.append({"role": "user", "content": prompt})
        return self.check(messages)
