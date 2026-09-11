class KeyboardRowShiftCipher:
    def __init__(self):
        row1_lower = "qwertyuiop"
        row2_lower = "asdfghjkl"
        row3_lower = "zxcvbnm"
        self.enc_map = {}
        self.dec_map = {}

        for row in (row1_lower, row2_lower, row3_lower):
            n = len(row)
            for i, ch in enumerate(row):
                enc = row[(i + 1) % n]
                dec = row[(i - 1) % n]
                self.enc_map[ch] = enc
                self.dec_map[enc] = ch
                self.enc_map[ch.upper()] = enc.upper()
                self.dec_map[enc.upper()] = ch.upper()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.dec_map.get(ch, ch) for ch in ciphertext)
