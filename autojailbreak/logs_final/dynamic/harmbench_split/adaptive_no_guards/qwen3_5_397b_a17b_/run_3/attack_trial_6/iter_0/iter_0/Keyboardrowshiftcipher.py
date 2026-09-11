class KeyboardRowShiftCipher:
    def __init__(self):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        self.enc_map = {}
        self.dec_map = {}
        for row in (row1, row2, row3):
            for i, ch in enumerate(row):
                enc = row[(i + 1) % len(row)]
                dec = row[(i - 1) % len(row)]
                self.enc_map[ch] = enc
                self.dec_map[ch] = dec

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            low = ch.lower()
            if low in self.enc_map and ch.isalpha():
                mapped = self.enc_map[low]
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            low = ch.lower()
            if low in self.dec_map and ch.isalpha():
                mapped = self.dec_map[low]
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)
