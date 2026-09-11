from models.api_model import OpenRouterModel
import re
from rapidfuzz.distance import Levenshtein
from wordfreq import zipf_frequency
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

FORMAT_PLACEHOLDER = "{text}"
REFUSAL = "REFUSAL"

SYSTEM_PROMPT_PATH = "denoiser/prompts/prompt.txt"
FORMAT_PROMPT_PATH = "denoiser/prompts/format.txt"


class LLMDenoiser:
    def __init__(self, system_prompt_path=SYSTEM_PROMPT_PATH, format_prompt_path=FORMAT_PROMPT_PATH, model_name="openai/gpt-4o-mini", max_new_tokens=1024, seed=0):
        self.model = OpenRouterModel(model_name=model_name, max_new_tokens=max_new_tokens, reasoning=False, seed=seed)
        self.system_prompt = self.load_prompt(system_prompt_path)
        self.format_prompt = self.load_prompt(format_prompt_path)

    def load_prompt(self, prompt_path):
        with open(prompt_path, "r") as f:
            prompt = f.read()
        return prompt
    
    @staticmethod
    def is_english(text, threshold=0.6):
        words = re.findall(r"[a-zA-Z']+", text.lower())

        if len(words) < 3:
            return False

        known = sum(
            zipf_frequency(word, "en") > 2.5
            for word in words
        )
        return known / len(words) >= threshold
    
    
    @staticmethod
    def normalize(text: str) -> str:
        text = text.lower().strip()
        text = re.sub(r"\s+", " ", text)
        return text


    @staticmethod
    def too_different(source: str, response: str, threshold: float = 0.75) -> bool:
        s1 = LLMDenoiser.normalize(source)
        s2 = LLMDenoiser.normalize(response)
        lscore = Levenshtein.normalized_similarity(s1, s2)
        return lscore < threshold
    

    def denoise(self, cipher, english):
        is_cipher_en = self.is_english(cipher)
        is_english_en = self.is_english(english)
        prompt = None
        if is_cipher_en and is_english_en:
            return english
        elif is_cipher_en:
            prompt = self.format_prompt.replace(FORMAT_PLACEHOLDER, cipher)
        else:
            prompt = self.format_prompt.replace(FORMAT_PLACEHOLDER, english)
        try:
            response = self.model.ask(self.system_prompt, prompt)
            if response == REFUSAL:
                return english if is_english_en else cipher
            if is_english_en:
                if self.too_different(english, response):
                    return english
            else:
                if self.too_different(cipher, response):
                    return cipher

            return response
        
        except Exception as e:
            print(f"Error occurred while denoising: {e}")
            return english if is_english_en else cipher
