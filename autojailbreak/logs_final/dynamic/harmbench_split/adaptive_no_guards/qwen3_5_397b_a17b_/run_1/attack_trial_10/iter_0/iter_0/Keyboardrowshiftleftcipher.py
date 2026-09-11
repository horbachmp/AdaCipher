class KeyboardRowShiftLeftCipher:
    def __init__(self):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        self.enc_map = {}
        self.dec_map = {}

        for row in (row1, row2, row3):
            n = len(row)
            for i, ch in enumerate(row):
                left = row[(i - 1) % n]
                right = row[(i + 1) % n]
                self.enc_map[ch] = left
                self.dec_map[left] = ch
                self.enc_map[ch.upper()] = left.upper()
                self.dec_map[left.upper()] = ch.upper()
                self.dec_map[ch] = right
                self.enc_map[right] = ch
                self.dec_map[ch.upper()] = right.upper()
                self.enc_map[right.upper()] = ch.upper()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.dec_map.get(ch, ch) for ch in ciphertext)
