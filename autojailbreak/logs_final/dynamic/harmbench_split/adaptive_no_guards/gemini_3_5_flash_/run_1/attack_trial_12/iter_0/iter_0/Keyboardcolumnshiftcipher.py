class KeyboardColumnShiftCipher:
    def __init__(self):
        self.encrypt_map = {
            "q": "a", "a": "z", "z": "q",
            "w": "s", "s": "x", "x": "w",
            "e": "d", "d": "c", "c": "e",
            "r": "f", "f": "v", "v": "r",
            "t": "g", "g": "b", "b": "t",
            "y": "h", "h": "n", "n": "y",
            "u": "j", "j": "m", "m": "u",
            "i": "k", "k": "i",
            "o": "l", "l": "o",
            "p": "p",
        }
        self.decrypt_map = {v: k for k, v in self.encrypt_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            lower = ch.lower()
            if lower in self.encrypt_map:
                mapped = self.encrypt_map[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            lower = ch.lower()
            if lower in self.decrypt_map:
                mapped = self.decrypt_map[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
