
import json

from guardrail.guard_decision import GuardDecision

CONTENT_FLAG = "content"
ROLE_FLAG = "role"

USER_ROLE = "user"
ASSISTANT_ROLE = "assistant"

INPUT_BLOCK = "Input blocked by guardrail"
OUTPUT_BLOCK = "Output blocked by guardrail"

ADDITIONAL_INFO_PREFIX = "Answer before block: "


class Target():
    def __init__(self, model, system_prompt, few_shot, benign_few_shot=None, guard=None, use_input_guard=None, use_output_guard=None):
        self.model = model
        self.system_prompt = system_prompt
        self.few_shot = few_shot
        self.ciphered_few_shot = []
        self.benign_few_shot = benign_few_shot
        self.guard = guard
        self.use_input_guard = use_input_guard
        self.use_output_guard = use_output_guard

        # which sides of the few-shot examples are enciphered (see set_cipher_flags);
        # both by default, i.e. the "cc" behaviour
        self.ciphered_input_flag = True
        self.ciphered_output_flag = True

    def set_cipher_flags(self, ciphered_input_flag, ciphered_output_flag):
        """Set from the static 'cipher_flag' config field.

        The few-shot examples must look like the conversation they demonstrate: user
        turns are enciphered only when the input is, assistant turns only when the
        output is.
        """
        self.ciphered_input_flag = ciphered_input_flag
        self.ciphered_output_flag = ciphered_output_flag

    def _cipher_sample(self, sample, cipher):
        """Encipher one few-shot message, unless its side is kept plain."""
        if sample[ROLE_FLAG] == ASSISTANT_ROLE:
            encipher = self.ciphered_output_flag
        else:
            encipher = self.ciphered_input_flag

        content = sample[CONTENT_FLAG]
        if encipher:
            content = cipher.encrypt(content)
        return {ROLE_FLAG: sample[ROLE_FLAG], CONTENT_FLAG: content}

    def cipher_few_shot(self, cipher):
        self.ciphered_few_shot = []
        for sample in self.few_shot:
            self.ciphered_few_shot.append(self._cipher_sample(sample, cipher))


    def cipher_benign_few_shot(self, cipher):
        self.ciphered_benign_few_shot = []
        for sample in self.benign_few_shot:
            self.ciphered_benign_few_shot.append(self._cipher_sample(sample, cipher))

    def _run_input_guard(self, question, current_system_prompt, few_shot):
        if not self.use_input_guard or self.guard is None:
            return GuardDecision(allowed=True)
        return self.guard.check_input(question, current_system_prompt, few_shot)

    def _run_output_guard(self, question, answer, current_system_prompt, few_shot):
        if not self.use_output_guard or self.guard is None:
            return GuardDecision(allowed=True)
        return self.guard.check_output(question, answer, current_system_prompt, few_shot)

    def ask(self, question, cipher_prompt, benign=False):
        current_system_prompt = cipher_prompt + self.system_prompt

        if benign:
            few_shot = self.ciphered_benign_few_shot
            sys_prompt_for_guard = self.system_prompt
        else:
            few_shot = self.ciphered_few_shot
            sys_prompt_for_guard = current_system_prompt

        # input guard checks user-controlled content
        input_decision = self._run_input_guard(
            question=question,
            current_system_prompt=sys_prompt_for_guard,
            few_shot=few_shot,
        )
        if not input_decision.allowed:
            additional_info = self._build_guard_additional_info(input_decision)
            return INPUT_BLOCK, additional_info

        # model call
        if benign:
            answer = self.model.ask(question, self.system_prompt, self.ciphered_benign_few_shot)
        else:
            answer = self.model.ask(question, current_system_prompt, self.ciphered_few_shot)

        # output guard checks assistant response in context
        output_decision = self._run_output_guard(
            question=question,
            answer=answer,
            current_system_prompt=sys_prompt_for_guard,
            few_shot=few_shot,
        )
        if not output_decision.allowed:
            additional_info = self._build_guard_additional_info(output_decision, answer)
            return OUTPUT_BLOCK, additional_info

        return answer, None

    def _build_guard_additional_info(self, decision, answer=None):
        """Build additional info JSON from GuardDecision fields (excluding allowed)"""
        info = {}
        if decision.category is not None:
            info["guard_category"] = decision.category
        if decision.reason is not None:
            info["guard_reason"] = decision.reason
        if decision.raw is not None:
            info["guard_raw"] = decision.raw
        if answer is not None:
            info["answer_before_block"] = answer
        return json.dumps(info, ensure_ascii=False) if info else None

