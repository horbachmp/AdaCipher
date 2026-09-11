from judges.judge import BaseJudge


class HarmBenchJudge(BaseJudge):
    def __init__(self, model, system_prompt, few_shot):
        super().__init__(model, system_prompt, few_shot)

    def process_prompt(self, question, response):
        return self.system_prompt.replace("{behavior}", question).replace("{generation}", response)

    def judge(self, question, response):
        formatted_prompt = self.process_prompt(question, response)
        return self.model.ask(formatted_prompt, "", self.few_shot)
