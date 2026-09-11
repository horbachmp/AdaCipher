class KeyboardRowShiftCipher:
    def __init__(self):
        self.rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        self.encrypt_map = {}
        self.decrypt_map = {}
        for row in self.rows:
            n = len(row)
            for i, ch in enumerate(row):
                enc = row[(i + 1) % n]
                dec = row[(i - 1) % n]
                self.encrypt_map[ch] = enc
                self.decrypt_map[ch] = dec

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            low = ch.lower()
            if low in self.encrypt_map:
                mapped = self.encrypt_map[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            low = ch.lower()
            if low in self.decrypt_map:
                mapped = self.decrypt_map[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
