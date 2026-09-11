class KeyboardRowShift:
    def __init__(self):
        self._rows = [
            "qwertypoiu",
            "asdfghjkl",
            "zxcvbnm",
        ]
        self._enc = {}
        self._dec = {}
        for row in self._rows:
            n = len(row)
            for i, ch in enumerate(row):
                self._enc[ch] = row[(i + 1) % n]
                self._dec[ch] = row[(i - 1) % n]

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
