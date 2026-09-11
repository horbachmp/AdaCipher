class HomoglyphLookalikeSubstitution:
    def __init__(self):
        self._enc_map = {
            "a": "а",
            "c": "с",
            "e": "е",
            "o": "о",
            "p": "р",
            "x": "х",
            "y": "у",
            "A": "А",
            "C": "С",
            "E": "Е",
            "O": "О",
            "P": "Р",
            "X": "Х",
            "S": "Ѕ",
        }
        self._dec_map = {v: k for k, v in self._enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec_map.get(ch, ch) for ch in ciphertext)
