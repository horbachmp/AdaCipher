class VowelIndexSubstitutionCipher:
    def __init__(self):
        self.encrypt_map = {
            "a": "1", "e": "2", "i": "3", "o": "4", "u": "5",
            "A": "1", "E": "2", "I": "3", "O": "4", "U": "5",
        }
        self.decrypt_map = {
            "1": "a", "2": "e", "3": "i", "4": "o", "5": "u",
        }

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.encrypt_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.decrypt_map.get(char, char) for char in ciphertext)
