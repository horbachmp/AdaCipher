class HomoglyphMixedAlphabetCipher:
    def __init__(self):
        self._enc_map = {
            "a": "а",
            "e": "е",
            "o": "о",
            "p": "р",
            "x": "х",
            "y": "у",
        }
        self._dec_map = {v: k for k, v in self._enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec_map.get(char, char) for char in ciphertext)
