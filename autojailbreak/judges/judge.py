
class BaseJudge():
    def __init__(self, model, system_prompt, few_shot):
        self.model = model
        self.system_prompt = system_prompt
        self.few_shot = few_shot

    def process_prompt(self, question, response):
        raise NotImplementedError("Subclasses must implement process_prompt")

    def judge(self, question, response):
        raise NotImplementedError("Subclasses must implement judge")




