class KeyboardRowShiftCipher:
    def __init__(self):
        self._enc_lower = {
            "q": "w", "w": "e", "e": "r", "r": "t", "t": "y", "y": "u", "u": "i", "i": "o", "o": "p", "p": "q",
            "a": "s", "s": "d", "d": "f", "f": "g", "g": "h", "h": "j", "j": "k", "k": "l", "l": "a",
            "z": "x", "x": "c", "c": "v", "v": "b", "b": "n", "n": "m", "m": "z",
        }
        self._dec_lower = {v: k for k, v in self._enc_lower.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._enc_lower.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._dec_lower.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
