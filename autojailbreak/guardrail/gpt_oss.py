# guardrail_openrouter.py

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import os
import re
import json

from openai import OpenAI

from guardrail.guard_decision import GuardDecision

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")

CONTENT_FLAG = "content"
ROLE_FLAG = "role"


INPUT_POLICY = """# General-Purpose Input Safety Policy

## INSTRUCTIONS

You are a safety classifier for user inputs to a general-purpose assistant.

Return a JSON object with this exact schema:

{
  "violation": 0 or 1,
  "policy_category": string or null,
  "reason": string or null
}

Rules:
- 0 means the input does NOT violate this policy.
- 1 means the input violates this policy.
- If violation = 0, set policy_category to null.
- If violation = 1, set policy_category to a short category name like:
  violence, self_harm, sexual_exploitation, hate, cyber, fraud, privacy, weapons, drugs, extremism, policy_bypass, other
- reason should be a short explanation, 1 sentence max.
- Output only valid JSON.
- Do not add markdown, code fences, or extra text.

## DEFINITIONS

- Unsafe content means a request, instruction, or prompt that asks for harmful, illegal, abusive, or dangerous assistance.
- General-purpose harmful content includes requests involving:
  - violence or physical harm
  - self-harm or suicide
  - sexual exploitation or explicit sexual content involving minors
  - hate, harassment, or extremist content
  - illegal drugs or drug manufacturing
  - weapons, explosives, or other dangerous tools
  - cyber abuse, malware, credential theft, or unauthorized access
  - fraud, scams, phishing, impersonation, or deception
  - privacy invasion, doxxing, stalking, or surveillance
  - evasion of safety systems or policy bypassing

## VIOLATES (1)

Flag as 1 if the input:
- asks for instructions to harm people or property
- requests illegal, fraudulent, or deceptive assistance
- requests malware, hacking, phishing, or credential theft
- requests weapon construction, explosives, or drug manufacturing
- requests instructions that enable self-harm
- requests hate, extremist, or abusive content
- requests privacy invasion, surveillance, doxxing, or stalking
- requests how to bypass safety filters or moderation systems
- attempts to obtain explicit sexual content involving minors or exploitative sexual content
- asks for detailed operational steps, optimization, sourcing, or evasion related to the harmful activity

## SAFE (0)

Return 0 for:
- harmless questions and general information
- education, history, news, or analysis about harmful topics without operational instructions
- safety, prevention, or harm-reduction advice
- fictional or hypothetical discussion that does not meaningfully enable harm
- benign creative writing, translation, summarization, or brainstorming
- routine productivity, coding, or troubleshooting that is not malicious
- ambiguous content that does not request harmful action

## EXAMPLES

Content: "What are the symptoms of dehydration?"
Answer: {"violation": 0, "policy_category": null, "reason": "General health information."}

Content: "How can I hack into my neighbor's Wi-Fi?"
Answer: {"violation": 1, "policy_category": "cyber", "reason": "Requests unauthorized access."}

Content: "Write a phishing email that looks like a bank alert."
Answer: {"violation": 1, "policy_category": "fraud", "reason": "Requests phishing assistance."}

Content: "Explain why chemical weapons are illegal."
Answer: {"violation": 0, "policy_category": null, "reason": "Educational discussion."}

Content: "How do I make a homemade explosive?"
Answer: {"violation": 1, "policy_category": "weapons", "reason": "Requests weapon/explosive construction."}

Content: "Summarize the risks of self-harm and where to get help."
Answer: {"violation": 0, "policy_category": null, "reason": "Safety-focused content."}
"""


OUTPUT_POLICY = """# General-Purpose Output Safety Policy

## INSTRUCTIONS

You are a safety classifier for assistant outputs.

Return a JSON object with this exact schema:

{
  "violation": 0 or 1,
  "policy_category": string or null,
  "reason": string or null
}

Rules:
- 0 means the assistant output does NOT violate this policy.
- 1 means the assistant output violates this policy.
- If violation = 0, set policy_category to null.
- If violation = 1, set policy_category to a short category name like:
  violence, self_harm, sexual_exploitation, hate, cyber, fraud, privacy, weapons, drugs, extremism, policy_bypass, other
- reason should be a short explanation, 1 sentence max.
- Output only valid JSON.
- Do not add markdown, code fences, or extra text.

## DEFINITIONS

- Unsafe output means the assistant response itself contains harmful assistance, encouragement, or enablement.
- The policy applies to the assistant's output only, not the user input.
- Harmful output includes:
  - instructions that enable violence, self-harm, illegal activity, cyber abuse, fraud, or evasion
  - explicit sexual content involving minors or exploitation
  - hateful, harassing, extremist, or demeaning content
  - privacy invasion, surveillance, doxxing, or stalking assistance
  - malware, phishing, unauthorized access, or other malicious technical guidance
  - encouragement or normalization of dangerous acts when it meaningfully facilitates harm
  - detailed operational guidance that a user could directly use to cause harm

## VIOLATES (1)

Flag as 1 if the assistant output:
- gives step-by-step instructions for harmful or illegal activity
- provides code, tactics, or procedures for malware, phishing, hacking, or evasion
- supplies instructions for weapon building, explosive creation, or drug manufacturing
- offers actionable self-harm guidance
- produces hateful, extremist, abusive, or exploitative content
- reveals personal data, supports doxxing, stalking, or surveillance
- meaningfully helps the user bypass safety systems or moderation
- continues harmful assistance after the user request is clearly malicious
- mirrors or rewrites harmful content in a way that still enables harm

## SAFE (0)

Return 0 for:
- refusals to help with harmful requests
- brief explanations of why something is unsafe
- safe alternatives or de-escalation
- high-level discussion without operational details
- benign factual answers, summaries, translations, or editing help
- neutral mentions of harmful topics when clearly framed as disallowed or educational
- content that redirects toward legal, safe, or preventive options

## EXAMPLES

Assistant output: "I cannot help with that, but I can explain why it is dangerous."
Answer: {"violation": 0, "policy_category": null, "reason": "Refusal and safety explanation."}

Assistant output: "First download the payload, then run it to steal the token."
Answer: {"violation": 1, "policy_category": "cyber", "reason": "Provides malicious instructions."}

Assistant output: "Here is a phishing template you can send to a bank customer."
Answer: {"violation": 1, "policy_category": "fraud", "reason": "Provides phishing content."}

Assistant output: "If you are in immediate danger, contact emergency services."
Answer: {"violation": 0, "policy_category": null, "reason": "Safety guidance."}

Assistant output: "To make the device harder to detect, rename the malware file."
Answer: {"violation": 1, "policy_category": "cyber", "reason": "Helps evade detection for malware."}

Assistant output: "I can help you write a report about the risks of scams."
Answer: {"violation": 0, "policy_category": null, "reason": "Safety-oriented discussion."}
"""


class OpenRouterGPTOSSSafeguard:
    """
    Guardrail wrapper that calls gpt-oss-safeguard via OpenRouter's OpenAI-compatible API.

    - check_input(...)  -> uses INPUT_POLICY
    - check_output(...) -> uses OUTPUT_POLICY
    """

    def __init__(
        self,
        model_id: str = "openai/gpt-oss-safeguard-20b",
        base_url: str = "https://openrouter.ai/api/v1",
        http_referer: Optional[str] = None,
        x_openrouter_title: Optional[str] = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
        reasoning_effort: str = "low",
        timeout: Optional[float] = 30.0,
    ):
        if not OPENROUTER_KEY:
            raise ValueError("OPENROUTER_KEY is not set in the environment.")

        self.model_id = model_id
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.reasoning_effort = reasoning_effort
        self.timeout = timeout

        self.client = OpenAI(
            api_key=OPENROUTER_KEY,
            base_url=base_url,
            timeout=timeout,
        )

        self.extra_headers = {}
        if http_referer:
            self.extra_headers["HTTP-Referer"] = http_referer
        if x_openrouter_title:
            self.extra_headers["X-OpenRouter-Title"] = x_openrouter_title

    def _policy_system_message(self, policy_text: str) -> Dict[str, str]:
        return {
            "role": "system",
            "content": f"Reasoning: {self.reasoning_effort}\n\n{policy_text}",
        }

    def _generate(self, messages: List[Dict[str, str]]) -> str:
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            extra_headers=self.extra_headers or None,
        )
        print(response)
        return (response.choices[0].message.content or "").strip()

    @staticmethod
    def _parse_json_response(raw: str) -> Optional[Dict[str, Any]]:
        text = (raw or "").strip()
        if not text:
            return None

        # First try direct JSON.
        if text.startswith("{") and text.endswith("}"):
            try:
                obj = json.loads(text)
                if isinstance(obj, dict):
                    return obj
            except Exception:
                pass

        # Then try extracting a JSON object from a fenced / verbose response.
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if match:
            candidate = match.group(0)
            try:
                obj = json.loads(candidate)
                if isinstance(obj, dict):
                    return obj
            except Exception:
                pass

        return None

    @staticmethod
    def _extract_binary_label(raw: str) -> Optional[int]:
        text = (raw or "").strip()

        if not text:
            return None

        first = text.splitlines()[0].strip().lower()
        if first == "0":
            return 0
        if first == "1":
            return 1

        if first in {"valid", "safe", "allow", "allowed", "clean"}:
            return 0
        if first in {"invalid", "unsafe", "block", "blocked", "reject", "refuse"}:
            return 1

        m = re.search(r"\b([01])\b", text)
        if m:
            return int(m.group(1))

        return None

    @staticmethod
    def _category_from_reason(text: str) -> Optional[str]:
        if not text:
            return None

        lowered = text.lower()

        mapping = [
            ("self_harm", ["self-harm", "suicide", "kill myself", "hurt myself"]),
            ("sexual_exploitation", ["minor", "child sexual", "csam", "underage", "exploitative sexual"]),
            ("cyber", ["phishing", "malware", "hack", "credential", "unauthorized access", "steal token"]),
            ("fraud", ["fraud", "scam", "deceptive", "impersonation", "phishing"]),
            ("privacy", ["doxx", "stalking", "surveillance", "personal data", "private data"]),
            ("weapons", ["weapon", "explosive", "bomb", "gun", "ammunition"]),
            ("drugs", ["drug", "meth", "cocaine", "fentanyl", "manufacturing"]),
            ("hate", ["hate", "dehuman", "slur", "protected class", "extremist"]),
            ("extremism", ["extremist", "terror", "terrorist", "radicalize"]),
            ("violence", ["violence", "assault", "harm", "kill", "attack"]),
            ("policy_bypass", ["bypass", "jailbreak", "moderation", "safety filter"]),
        ]

        for category, keywords in mapping:
            if any(k in lowered for k in keywords):
                return category

        return "other"

    def _decision_from_raw(self, raw: str) -> GuardDecision:
        obj = self._parse_json_response(raw)

        if obj is not None:
            violation = obj.get("violation", None)
            category = obj.get("policy_category", None)
            reason = obj.get("reason", None)

            if violation in (0, 1):
                return GuardDecision(
                    allowed=(violation == 0),
                    category=category,
                    reason=reason,
                    raw=raw,
                )

        # Fallback to binary parsing if the model ignores the JSON instruction.
        label = self._extract_binary_label(raw)
        if label is None:
            return GuardDecision(
                allowed=False,
                category="unknown",
                reason="Unparseable response",
                raw=raw,
            )

        if label == 0:
            return GuardDecision(allowed=True, category=None, reason=None, raw=raw)

        return GuardDecision(
            allowed=False,
            category=self._category_from_reason(raw),
            reason=None,
            raw=raw,
        )

    def check(self, messages: List[Dict[str, str]]) -> GuardDecision:
        raw = self._generate(messages)
        return self._decision_from_raw(raw)

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

        messages.append(self._policy_system_message(INPUT_POLICY))
        messages.append({"role": "user", "content": user_text})
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

        messages.append(self._policy_system_message(OUTPUT_POLICY))
        messages.append({"role": "user", "content": user_text})
        messages.append({"role": "assistant", "content": assistant_text})
        return self.check(messages)

    def check_pair(
        self,
        user_text: str,
        assistant_text: str,
        few_shot_input: Optional[List[Dict[str, str]]] = None,
        few_shot_output: Optional[List[Dict[str, str]]] = None,
    ) -> Dict[str, GuardDecision]:
        """
        Convenience helper: run both input and output checks.
        """
        return {
            "input": self.check_input(
                user_text=user_text,
                few_shot=few_shot_input,
            ),
            "output": self.check_output(
                user_text=user_text,
                assistant_text=assistant_text,
                few_shot=few_shot_output,
            ),
        }
