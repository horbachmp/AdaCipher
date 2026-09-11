class QwertyShiftLeftCipher:
    def __init__(self):
        self._enc = {}
        self._dec = {}
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for row in rows:
            n = len(row)
            for i, ch in enumerate(row):
                left = row[(i - 1) % n]
                right = row[(i + 1) % n]
                self._enc[ch] = left
                self._dec[ch] = right

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._enc.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._dec.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
