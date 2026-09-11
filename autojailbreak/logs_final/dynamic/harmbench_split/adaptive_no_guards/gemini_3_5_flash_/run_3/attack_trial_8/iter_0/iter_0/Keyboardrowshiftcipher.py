class KeyboardRowShiftCipher:
    def __init__(self):
        self._enc = {}
        self._dec = {}

        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        for row in rows:
            n = len(row)
            for i, ch in enumerate(row):
                self._enc[ch] = row[(i + 1) % n]
                self._dec[ch] = row[(i - 1) % n]

        self._enc.update({k.upper(): v.upper() for k, v in list(self._enc.items())})
        self._dec.update({k.upper(): v.upper() for k, v in list(self._dec.items())})

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec.get(ch, ch) for ch in ciphertext)
