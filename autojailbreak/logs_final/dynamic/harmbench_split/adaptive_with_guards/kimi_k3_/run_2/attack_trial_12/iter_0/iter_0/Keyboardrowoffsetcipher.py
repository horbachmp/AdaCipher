class KeyboardRowOffsetCipher:
    def __init__(self):
        self.encrypt_map = {}
        self.decrypt_map = {}

        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]

        for row in rows:
            n = len(row)
            for i, ch in enumerate(row):
                enc = row[(i + 1) % n]
                dec = row[(i - 1) % n]
                self.encrypt_map[ch] = enc
                self.decrypt_map[ch] = dec
                self.encrypt_map[ch.upper()] = enc.upper()
                self.decrypt_map[ch.upper()] = dec.upper()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.encrypt_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.decrypt_map.get(ch, ch) for ch in ciphertext)
