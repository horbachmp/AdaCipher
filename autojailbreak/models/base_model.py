from models.logger import ModelLogger


class Model():
    def __init__(self, model_name, max_new_tokens, seed=0, temperature=0.0, enable_logging=True):
        self.model_name = model_name
        self.max_new_tokens = max_new_tokens
        self.seed = seed
        self.temperature = temperature

        # Initialize the logger if logging is enabled
        self.logger = None
        self.model_run_id = None
        if enable_logging:
            self.logger = ModelLogger(
                model_name=model_name,
                max_new_tokens=max_new_tokens,
                seed=seed,
                temperature=temperature
            )
            self.model_run_id = self.logger.model_run_id

    def ask(self, question, system_prompt, few_shot):
        pass
