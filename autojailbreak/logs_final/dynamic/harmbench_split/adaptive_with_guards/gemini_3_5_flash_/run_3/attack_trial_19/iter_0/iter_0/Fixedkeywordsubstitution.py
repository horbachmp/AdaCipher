class FixedKeywordSubstitution:
    def __init__(self):
        keyword = "DANGER"
        seen = set()
        cipher_alpha = []
        for ch in keyword.upper():
            if ch not in seen and ch.isalpha():
                seen.add(ch)
                cipher_alpha.append(ch)
        for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if ch not in seen:
                seen.add(ch)
                cipher_alpha.append(ch)
        self.enc_upper = {plain: subst for plain, subst in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", cipher_alpha)}
        self.dec_upper = {subst: plain for plain, subst in self.enc_upper.items()}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.isalpha():
                if ch.isupper():
                    out.append(self.enc_upper[ch])
                else:
                    out.append(self.enc_upper[ch.upper()].lower())
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch.isalpha():
                if ch.isupper():
                    out.append(self.dec_upper[ch])
                else:
                    out.append(self.dec_upper[ch.upper()].lower())
            else:
                out.append(ch)
        return "".join(out)
