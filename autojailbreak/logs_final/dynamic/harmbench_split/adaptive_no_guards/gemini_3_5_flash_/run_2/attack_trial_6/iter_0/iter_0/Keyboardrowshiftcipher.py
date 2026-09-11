class KeyboardRowShiftCipher:
    def __init__(self):
        self._encrypt_map = {}
        self._decrypt_map = {}

        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]

        for row in rows:
            n = len(row)
            for i, ch in enumerate(row):
                self._encrypt_map[ch] = row[(i + 1) % n]
                self._decrypt_map[ch] = row[(i - 1) % n]

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._encrypt_map.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._decrypt_map.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
