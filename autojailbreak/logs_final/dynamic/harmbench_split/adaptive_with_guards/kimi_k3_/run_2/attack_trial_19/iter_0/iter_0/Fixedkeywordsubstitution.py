class FixedKeywordSubstitution:
    def __init__(self):
        keyword = "CIPHER"
        seen = set()
        cipher_alpha = []
        for ch in keyword:
            ch = ch.upper()
            if ch not in seen and ch.isalpha():
                seen.add(ch)
                cipher_alpha.append(ch)
        for i in range(26):
            ch = chr(ord('A') + i)
            if ch not in seen:
                cipher_alpha.append(ch)
        plain_alpha = [chr(ord('A') + i) for i in range(26)]
        self.enc_upper = {p: c for p, c in zip(plain_alpha, cipher_alpha)}
        self.dec_upper = {c: p for p, c in zip(plain_alpha, cipher_alpha)}
        self.enc_lower = {p.lower(): c.lower() for p, c in self.enc_upper.items()}
        self.dec_lower = {c.lower(): p.lower() for c, p in self.dec_upper.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if 'A' <= ch <= 'Z':
                result.append(self.enc_upper.get(ch, ch))
            elif 'a' <= ch <= 'z':
                result.append(self.enc_lower.get(ch, ch))
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if 'A' <= ch <= 'Z':
                result.append(self.dec_upper.get(ch, ch))
            elif 'a' <= ch <= 'z':
                result.append(self.dec_lower.get(ch, ch))
            else:
                result.append(ch)
        return ''.join(result)
