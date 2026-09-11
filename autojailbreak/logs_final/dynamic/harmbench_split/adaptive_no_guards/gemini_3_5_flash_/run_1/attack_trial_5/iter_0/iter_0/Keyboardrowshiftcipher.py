class KeyboardRowShiftCipher:
    def __init__(self):
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        self.encrypt_map = {}
        self.decrypt_map = {}
        for row in rows:
            n = len(row)
            for i, ch in enumerate(row):
                self.encrypt_map[ch] = row[(i + 1) % n]
                self.decrypt_map[ch] = row[(i - 1) % n]

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self.encrypt_map.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self.decrypt_map.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
