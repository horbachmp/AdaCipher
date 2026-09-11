class AlternatingVowelConsonantShift:
    def __init__(self):
        self._enc = {
            "a": "e", "e": "i", "i": "o", "o": "u", "u": "a",
            "b": "c", "c": "d", "d": "f", "f": "g", "g": "h", "h": "j",
            "j": "k", "k": "l", "l": "m", "m": "n", "n": "p", "p": "q",
            "q": "r", "r": "s", "s": "t", "t": "v", "v": "w", "w": "x",
            "x": "y", "y": "z", "z": "b",
        }
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._enc.get(lower, lower)
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._dec.get(lower, lower)
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)
