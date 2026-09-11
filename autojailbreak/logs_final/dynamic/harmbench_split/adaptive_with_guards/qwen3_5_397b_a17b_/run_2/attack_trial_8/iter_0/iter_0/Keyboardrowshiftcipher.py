class KeyboardRowShiftCipher:
    def __init__(self):
        self.rows = [
            "qwertypoiu",
            "asdfghjkl",
            "zxcvbnm",
        ]
        self.enc_map = {}
        self.dec_map = {}
        for row in self.rows:
            n = len(row)
            for i, ch in enumerate(row):
                enc = row[(i + 1) % n]
                dec = row[(i - 1) % n]
                self.enc_map[ch] = enc
                self.dec_map[ch] = dec

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            lower = ch.lower()
            if lower in self.enc_map and ch.isalpha():
                mapped = self.enc_map[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            lower = ch.lower()
            if lower in self.dec_map and ch.isalpha():
                mapped = self.dec_map[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
