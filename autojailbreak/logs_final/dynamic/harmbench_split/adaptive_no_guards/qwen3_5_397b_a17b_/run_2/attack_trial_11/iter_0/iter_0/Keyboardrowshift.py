class KeyboardRowShift:
    def __init__(self):
        self.rows = [
            "QWERTYUIOP",
            "ASDFGHJKL",
            "ZXCVBNM",
        ]
        self.encrypt_map = {}
        self.decrypt_map = {}
        for row in self.rows:
            n = len(row)
            for i, ch in enumerate(row):
                self.encrypt_map[ch] = row[(i + 1) % n]
                self.decrypt_map[ch] = row[(i - 1) % n]

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            upper = ch.upper()
            if upper in self.encrypt_map and ch.isalpha():
                mapped = self.encrypt_map[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            upper = ch.upper()
            if upper in self.decrypt_map and ch.isalpha():
                mapped = self.decrypt_map[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)
