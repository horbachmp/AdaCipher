from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

from models.base_model import Model

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")

class OpenRouterModel(Model):
    def __init__(
        self,
        model_name: str = "",
        max_new_tokens: int = 512,
        reasoning: bool = False,
        seed: int = 0,
        temperature: float = 0.0,
        enable_logging: bool = True,
    ):

        super().__init__(model_name, max_new_tokens, seed, temperature, enable_logging=enable_logging)
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_KEY,
            )
        self.reasoning_enabled = reasoning
        self.reasoning = {"enabled": reasoning}
        if "gemini" in self.model_name.lower() or "gpt-oss-120b" in self.model_name.lower():
            self.reasoning = {"effort": "minimal"}
            # self.max_new_tokens = 1024

        # Update the logger with the additional reasoning parameter
        if self.logger:
            self.logger.config_params["reasoning"] = reasoning

        self.run_id = self.logger.model_run_id
        

    def ask(self, question: str, system_prompt: str = None, few_shot: list = None) -> str:

        if few_shot is None:
            few_shot = []

        # Log the request
        if self.logger:
            self.logger.log_request(
                question=question,
                system_prompt=system_prompt,
                few_shot=few_shot,
                temperature=self.temperature,
                seed=self.seed,
                reasoning=self.reasoning
            )

        try:
            if "gemini" in self.model_name.lower():
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        *few_shot,
                        {"role": "user", "content": question},
                    ],
                    max_completion_tokens=self.max_new_tokens,
                    temperature=self.temperature,
                    seed=self.seed,
                    extra_body={"reasoning": self.reasoning}
                )
            else:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        *few_shot,
                        {"role": "user", "content": question},
                    ],
                    max_tokens=self.max_new_tokens,
                    temperature=self.temperature,
                    seed=self.seed,
                    extra_body={"reasoning": self.reasoning}
                )

            content = response.choices[0].message.content
            if content is None or response.choices[0].finish_reason == 'refusal':
                result = "REFUSAL"
                if self.logger:
                    self.logger.log_response(
                        response=result,
                        success=False,
                        finish_reason=response.choices[0].finish_reason
                    )
                return result

            result = content.strip()
            if self.logger:
                self.logger.log_response(
                    response=result,
                    success=True,
                    finish_reason=response.choices[0].finish_reason,
                    model=response.model,
                    usage=response.usage.dict() if response.usage else None
                )
            return result

        except Exception as e:
            error_msg = str(e)
            if self.logger:
                self.logger.log_response(
                    response="",
                    success=False,
                    error=error_msg
                )
            print(e)
            print(f"Response:{response if 'response' in locals() else 'N/A'}")
            return str(e)
