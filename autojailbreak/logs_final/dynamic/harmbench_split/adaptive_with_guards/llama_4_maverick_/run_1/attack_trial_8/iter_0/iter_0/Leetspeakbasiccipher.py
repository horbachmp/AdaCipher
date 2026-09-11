class LeetSpeakBasicCipher:
    def __init__(self):
        self.encrypt_map = {
            "a": "4", "A": "4",
            "e": "3", "E": "3",
            "i": "1", "I": "1",
            "o": "0", "O": "0",
            "t": "7", "T": "7",
            "s": "5", "S": "5",
        }
        self.decrypt_map = {
            "4": "a",
            "3": "e",
            "1": "i",
            "0": "o",
            "7": "t",
            "5": "s",
        }

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.encrypt_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.decrypt_map.get(char, char) for char in ciphertext)
