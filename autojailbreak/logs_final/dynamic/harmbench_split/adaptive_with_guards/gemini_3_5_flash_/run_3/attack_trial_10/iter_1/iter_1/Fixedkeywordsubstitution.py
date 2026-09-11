class FixedKeywordSubstitution:
    def __init__(self):
        keyword = "SECURE"
        seen = set()
        cipher_letters = []
        for ch in keyword:
            if ch not in seen and ch.isalpha():
                seen.add(ch)
                cipher_letters.append(ch.lower())
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch not in seen:
                cipher_letters.append(ch)
        plain_letters = list("abcdefghijklmnopqrstuvwxyz")
        self.enc_lower = {p: c for p, c in zip(plain_letters, cipher_letters)}
        self.dec_lower = {c: p for p, c in zip(plain_letters, cipher_letters)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.islower():
                result.append(self.enc_lower.get(ch, ch))
            elif ch.isupper():
                result.append(self.enc_lower.get(ch.lower(), ch.lower()).upper())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.islower():
                result.append(self.dec_lower.get(ch, ch))
            elif ch.isupper():
                result.append(self.dec_lower.get(ch.lower(), ch.lower()).upper())
            else:
                result.append(ch)
        return "".join(result)
