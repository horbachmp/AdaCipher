class VowelRotatorWithConsonantStatic:
    def __init__(self):
        self.encrypt_map = str.maketrans({
            "a": "e",
            "e": "i",
            "i": "o",
            "o": "u",
            "u": "a",
            "A": "E",
            "E": "I",
            "I": "O",
            "O": "U",
            "U": "A",
        })
        self.decrypt_map = str.maketrans({
            "e": "a",
            "i": "e",
            "o": "i",
            "u": "o",
            "a": "u",
            "E": "A",
            "I": "E",
            "O": "I",
            "U": "O",
            "A": "U",
        })

    def encrypt(self, plaintext: str) -> str:
        return plaintext.translate(self.encrypt_map)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext.translate(self.decrypt_map)
