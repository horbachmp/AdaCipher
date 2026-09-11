class KeyboardRowShiftCipher:
    def __init__(self):
        self._encrypt_map = {
            "q": "w", "w": "e", "e": "r", "r": "t", "t": "y", "y": "u", "u": "i", "i": "o", "o": "p", "p": "q",
            "a": "s", "s": "d", "d": "f", "f": "g", "g": "h", "h": "j", "j": "k", "k": "l", "l": "a",
            "z": "x", "x": "c", "c": "v", "v": "b", "b": "n", "n": "m", "m": "z",
        }
        self._decrypt_map = {v: k for k, v in self._encrypt_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                lower = char.lower()
                mapped = self._encrypt_map.get(lower, lower)
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char.isalpha():
                lower = char.lower()
                mapped = self._decrypt_map.get(lower, lower)
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return "".join(result)
