import re
from pathlib import Path
import os
import importlib.util
import json

class Attacker():
    def __init__(self, model, code_system_prompt, few_shot, log_path):
        self.model = model
        self.code_system_prompt = code_system_prompt
        self.few_shot = few_shot
        self.log_path = log_path
        


    def save_model_code(self, response_text: str, name) -> str:
        """
        Extract Python code from a model response and save it to a .py file.

        Supports:
        - raw code
        - code fenced with ```python ... ```
        - code fenced with ``` ... ```
        """
        output_path = Path(os.path.join(self.log_path, "attacker_generated_code", f"{name}.py")) 

        code = response_text.strip()

        fence_match = re.search(
            r"```(?:python)?\s*(.*?)```",
            code,
            flags=re.DOTALL | re.IGNORECASE,
        )
        if fence_match:
            code = fence_match.group(1).strip()

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(code + "\n", encoding="utf-8")

        return str(path)
    
    def load_module_from_file(self, py_path: str):
        py_path = str(Path(py_path))
        module_name = Path(py_path).stem

        spec = importlib.util.spec_from_file_location(module_name, py_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    
    def test_cipher(self, tests, cipher_module):
        for test in tests:
            input = test["plaintext"]
            output = test["ciphertext"]
            gen_output = cipher_module.encrypt(input)
            assert gen_output == output



    def perform_attack(self, cipher_desciption):
        #get jsom from cipher description
        cipher_json = json.loads(cipher_desciption)
        print(cipher_json)
        print(cipher_json["name"])
        #generate code
        code = self.model.ask(cipher_desciption, self.code_system_prompt, self.few_shot)
        print(f"Code:{code}")
        cipher_module_path = self.save_model_code(code, cipher_json["name"])
        cipher_module = self.load_module_from_file(cipher_module_path)
        self.test_cipher(self.few_shot, cipher_module)
        
