from models.api_model import OpenRouterModel

FORMAT_PLACEHOLDER = "{text}"
REFUSAL = "REFUSAL"

SYSTEM_PROMPT_PATH = "summariser/prompts/new_system_prompt2.txt"
FORMAT_PROMPT_PATH = "summariser/prompts/format_prompt.txt"


class LLMSummariser:
    def __init__(self, system_prompt_path=SYSTEM_PROMPT_PATH, format_prompt_path=FORMAT_PROMPT_PATH, model_name="openai/gpt-4o-mini", max_new_tokens=512, seed=0):
        self.model = OpenRouterModel(model_name=model_name, max_new_tokens=max_new_tokens, reasoning=False, seed=seed)
        self.system_prompt = self.load_prompt(system_prompt_path)
        self.format_prompt = self.load_prompt(format_prompt_path)

    def load_prompt(self, prompt_path):
        with open(prompt_path, "r") as f:
            prompt = f.read()
        return prompt

    def summarise(self, text):
        prompt = self.format_prompt.replace(FORMAT_PLACEHOLDER, text)
        try:
            response = self.model.ask(self.system_prompt, prompt)
            if response == REFUSAL:
                return text
            return response
        except Exception as e:
            print(f"Error occurred while summarising: {e}")
            return text
