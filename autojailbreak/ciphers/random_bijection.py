import random
from string import Template

# TASK = "{task}"
RULES = "{rules}"
CIPHER_NAME = "{cipher_name}"


class RandomBijectionCipher:
    def __init__(self, seed=0):
        self.seed = seed

        # we set random bijection for all English letters based on the seed
        rng = random.Random(self.seed)
        letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        shuffled_letters = letters.copy()
        rng.shuffle(shuffled_letters)
        self.forward_mapping = {letters[i]: shuffled_letters[i] for i in range(26)}
        for letter in letters:
            self.forward_mapping[letter.upper()] = self.forward_mapping[letter].upper()
        self.backward_mapping = {v: k for k, v in self.forward_mapping.items()}
        

    def create_cipher_prompt(self, base_prompt):
        rules = ""
        # rules += "Plaintext: abcdefghijklmnopqrstuvwxyz\n"
        # rules += "Ciphertext: " + "".join([self.forward_mapping[chr(i)] for i in range(ord('a'), ord('z') + 1)]) + "\n\n"
        rules += "Plaintext alphabet:\n"
        rules += "".join([f"{chr(i)}" for i in range(ord('a'), ord('z') + 1)])
        rules += "\n\nCiphertext alphabet:\n"
        rules += "".join([f"{self.forward_mapping[chr(i)]}" for i in range(ord('a'), ord('z') + 1)])

        # task = "Encipher the input text using the above letter mappings."
        return base_prompt.replace(CIPHER_NAME, "Random Bijection").replace(RULES, rules.strip())



    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ciphertext += self.forward_mapping.get(char, char)
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                plaintext += self.backward_mapping.get(char, char)
            else:
                plaintext += char
        return plaintext            
