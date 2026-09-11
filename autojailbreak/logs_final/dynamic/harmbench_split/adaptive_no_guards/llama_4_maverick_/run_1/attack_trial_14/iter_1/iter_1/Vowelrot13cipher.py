class VowelRot13Cipher:
    def __init__(self):
        self.encrypt_map = {
            "a": "n", "e": "r", "i": "v", "o": "b", "u": "h",
            "A": "N", "E": "R", "I": "V", "O": "B", "U": "H",
        }
        self.decrypt_map = {v: k for k, v in self.encrypt_map.items()}

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.encrypt_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.decrypt_map.get(char, char) for char in ciphertext)
