class Base36DigitAndVowelSwap:
    def __init__(self):
        self.encrypt_map = {
            "A": "1",
            "a": "1",
            "E": "2",
            "e": "2",
            "I": "3",
            "i": "3",
            "O": "4",
            "o": "4",
            "U": "5",
            "u": "5",
        }
        self.decrypt_map = {
            "1": "a",
            "2": "e",
            "3": "i",
            "4": "o",
            "5": "u",
        }

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.encrypt_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.decrypt_map.get(ch, ch) for ch in ciphertext)
