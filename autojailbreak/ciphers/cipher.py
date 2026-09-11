import os
import json
import re
from typing import Any
from utils.code_module_utils import load_module_from_file
from utils.json_utils import extract_json


CIPHER_PROMPT_PLACEHOLDERS = ["name", "idea", "encrypt_rules", "decrypt_rules"]

# Characters allowed in text after sanitisation when a cipher operation fails.
# Keeps ASCII letters, digits, common punctuation, and whitespace.
_SAFE_CHARS_PATTERN = re.compile(r"[^a-zA-Z0-9 .,!?;:'\"()\-_\n\r\t]")


def _clean_text(text: str) -> str:
    """Remove characters that are likely to cause cipher implementation errors."""
    if not isinstance(text, str):
        return ""
    return _SAFE_CHARS_PATTERN.sub("", text)


class CipherBundle():
    def __init__(self, module_path, description_json, name, base_cipher_prompt):
        self.module_path = module_path
        cipher_class = load_module_from_file(module_path)
        self.cipher = cipher_class()
        self.description_json = description_json
        self.name = name
        self.base_cipher_prompt = base_cipher_prompt
        if self.name == "id":
            self.prompt = ""
        else:
            self.prompt = self.__format_cipher_prompt__()
        
    def extract_idea(self) -> str:
        """Extract the ``idea`` field from ``self.description_json``.

        Returns the ``idea`` value as a string, or an empty string if it cannot
        be found.
        """
        description = self.description_json
        if isinstance(description, dict):
            idea = description.get("idea")
            if isinstance(idea, str):
                return idea
            return ""

        if isinstance(description, str):
            parsed = extract_json(description)
            if isinstance(parsed, dict):
                idea = parsed.get("idea")
                if isinstance(idea, str):
                    return idea
            return ""

        return ""


    def __format_cipher_prompt__(self):
        prompt = self.base_cipher_prompt
        for placeholder in CIPHER_PROMPT_PLACEHOLDERS:
            prompt = prompt.replace("{" + placeholder + "}", self.description_json[placeholder])
        return prompt

    def encrypt(self, text: str) -> str:
        """Encrypt *text* via the underlying cipher.

        If the cipher raises an exception the text is cleaned of potentially
        dangerous characters and the operation is retried once.
        """
        try:
            return self.cipher.encrypt(text)
        except Exception as e:
            print(f"Cipher encryption failed with error: {e}. Retrying with cleaned text.")
            try:
                cleaned = _clean_text(text)
                return self.cipher.encrypt(cleaned)
            except Exception as e:
                print(f"Cipher encryption failed with error: {e}.")
                return f"Cipher encryption failed on text: {text}"


    def decrypt(self, text: str) -> str:
        """Decrypt *text* via the underlying cipher.

        If the cipher raises an exception the text is cleaned of potentially
        dangerous characters and the operation is retried once.
        """
        try:
            return self.cipher.decrypt(text)
        except Exception as e:
            print(f"Cipher decryption failed with error: {e}. Retrying with cleaned text.")
            print(f"Text: {text}")
            try:
                cleaned = _clean_text(text)
                return self.cipher.decrypt(cleaned)
            except Exception as e:
                print(f"Cipher decryption failed with error: {e}.")
                return f"Cipher decryption failed on cleaned text: {cleaned}"


    @classmethod
    def load(cls, bundle_path):
        """Recreate a bundle from a JSON file written by :meth:`save`."""
        with open(bundle_path, "r", encoding="utf-8") as f:
            bundle_data = json.load(f)

        missing = [k for k in ("name", "module_path", "description_json") if k not in bundle_data]
        if missing:
            raise ValueError(f"Cipher bundle '{bundle_path}' is missing required fields: {missing}")

        return cls(
            module_path=bundle_data["module_path"],
            description_json=bundle_data["description_json"],
            name=bundle_data["name"],
            base_cipher_prompt=bundle_data.get("base_cipher_prompt", ""),
        )


    def save(self, save_path):
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        bundle_data = {
            "name": self.name,
            "module_path": self.module_path,
            "description_json": self.description_json,
            "base_cipher_prompt": self.base_cipher_prompt,
            "prompt": self.prompt
        }
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(bundle_data, f, indent=2, ensure_ascii=False)
        print(f"Cipher bundle saved to {save_path}")
    
