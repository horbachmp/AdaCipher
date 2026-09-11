from judges.judge import BaseJudge


BASE_PROMPT = """
Here is tha data:

cipher_info: {cipher}

question: {question}

raw_response: {response}

decrypted response: {decrypted_response}
"""


class ProcessJudge(BaseJudge):
    def __init__(self, model, system_prompt, few_shot):
        super().__init__(model, system_prompt, few_shot)

    def process_prompt(self, cipher_info, question, raw_response, decrypted_response):
        return BASE_PROMPT.format(cipher=cipher_info, question=question, response=raw_response, decrypted_response=decrypted_response)

    def judge(self, cipher_info, question, raw_response, decrypted_response):
        formatted_prompt = self.process_prompt(cipher_info, question, raw_response, decrypted_response)
        return self.model.ask(formatted_prompt, self.system_prompt, self.few_shot)
