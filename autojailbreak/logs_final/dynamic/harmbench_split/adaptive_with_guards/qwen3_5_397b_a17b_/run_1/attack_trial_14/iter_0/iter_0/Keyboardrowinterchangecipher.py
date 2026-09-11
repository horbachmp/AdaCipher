class KeyboardRowInterchangeCipher:
    def __init__(self):
        self.row1 = "qwertyuiop"
        self.row2 = "asdfghjkl;"
        self.row3 = "zxcvbnm"
        self.row3_shifted = "xcvbnmz"
        self.enc_map = {}
        self.dec_map = {}

        for i, ch in enumerate(self.row1):
            mapped = self.row2[i]
            self.enc_map[ch] = mapped
            self.dec_map[mapped] = ch

        for i, ch in enumerate(self.row2):
            mapped = self.row1[i]
            self.enc_map[ch] = mapped
            self.dec_map[mapped] = ch

        for i, ch in enumerate(self.row3):
            mapped = self.row3_shifted[i]
            self.enc_map[ch] = mapped
            self.dec_map[mapped] = ch

    def encrypt(self, plaintext: str) -> str:
        out = []
        for char in plaintext:
            lower = char.lower()
            if lower in self.enc_map:
                mapped = self.enc_map[lower]
                out.append(mapped.upper() if char.isupper() else mapped)
            else:
                out.append(char)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for char in ciphertext:
            lower = char.lower()
            if lower in self.dec_map:
                mapped = self.dec_map[lower]
                out.append(mapped.upper() if char.isupper() else mapped)
            else:
                out.append(char)
        return "".join(out)
