class QwertyTwoKeyRightShiftCipher:
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
                enc = row[(i + 2) % n]
                dec = row[(i - 2) % n]
                self.encrypt_map[ch] = enc
                self.decrypt_map[ch] = dec

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
