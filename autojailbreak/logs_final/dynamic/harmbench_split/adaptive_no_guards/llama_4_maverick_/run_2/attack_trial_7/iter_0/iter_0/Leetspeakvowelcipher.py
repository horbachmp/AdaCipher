class LeetspeakVowelCipher:
    def __init__(self):
        self._enc = {
            "a": "4",
            "e": "3",
            "i": "1",
            "o": "0",
            "u": "5",
            "A": "4",
            "E": "3",
            "I": "1",
            "O": "0",
            "U": "5",
        }
        self._dec = {
            "4": "a",
            "3": "e",
            "1": "i",
            "0": "o",
            "5": "u",
        }

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec.get(ch, ch) for ch in ciphertext)
