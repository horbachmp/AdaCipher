class KeyboardShiftLeftCipher:
    def __init__(self):
        self.enc_map = {}
        self.dec_map = {}

        rows = [
            ("qwertyuiop", "p"),
            ("asdfghjkl", "l"),
            ("zxcvbnm", "m"),
        ]

        for row, wrap_left in rows:
            n = len(row)
            for i, ch in enumerate(row):
                enc = row[(i - 1) % n]
                dec = row[(i + 1) % n]
                self.enc_map[ch] = enc
                self.dec_map[ch] = dec
                self.enc_map[ch.upper()] = enc.upper()
                self.dec_map[ch.upper()] = dec.upper()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.dec_map.get(ch, ch) for ch in ciphertext)
