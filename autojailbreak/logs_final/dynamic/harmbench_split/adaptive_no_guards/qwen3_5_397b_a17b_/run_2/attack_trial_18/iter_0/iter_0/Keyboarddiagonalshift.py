class KeyboardDiagonalShift:
    def __init__(self):
        lower_encrypt = {
            "q": "a", "w": "s", "e": "d", "r": "f", "t": "g", "y": "h", "u": "j", "i": "k", "o": "l", "p": "z",
            "a": "x", "s": "c", "d": "v", "f": "b", "g": "n", "h": "m", "j": "q", "k": "w", "l": "e",
            "z": "r", "x": "t", "c": "y", "v": "u", "b": "i", "n": "o", "m": "p",
        }
        self._enc = {}
        self._dec = {}
        for k, v in lower_encrypt.items():
            self._enc[k] = v
            self._enc[k.upper()] = v.upper()
            self._dec[v] = k
            self._dec[v.upper()] = k.upper()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec.get(ch, ch) for ch in ciphertext)
