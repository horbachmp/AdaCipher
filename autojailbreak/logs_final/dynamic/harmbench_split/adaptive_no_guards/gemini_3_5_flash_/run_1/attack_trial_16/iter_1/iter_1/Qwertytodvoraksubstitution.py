class QwertyToDvorakSubstitution:
    def __init__(self):
        plain = "abcdefghijklmnopqrstuvwxyz"
        cipher = "abkeouidchtnumrlxpsygvwjfq"
        self._enc_lower = {p: c for p, c in zip(plain, cipher)}
        self._dec_lower = {c: p for p, c in zip(plain, cipher)}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._enc_lower.get(lower, lower)
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._dec_lower.get(lower, lower)
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)
