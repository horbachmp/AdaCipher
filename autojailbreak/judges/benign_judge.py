import re

from judges.judge import BaseJudge

PROMPT_TEMPLATE = """
[Question]
{question}
[The Start of Assistant’s Answer]
{answer}
[The End of Assistant’s Answer]
"""


class BenignJudge(BaseJudge):
    def __init__(self, model, system_prompt, few_shot):
        super().__init__(model, system_prompt, few_shot)


    def process_prompt(self, question, answer):
        return PROMPT_TEMPLATE.replace("{question}", question).replace("{answer}", answer)

    def judge(self, question, answer):
        formatted_prompt = self.process_prompt(question, answer)
        return self.model.ask(self.system_prompt, formatted_prompt, self.few_shot)
