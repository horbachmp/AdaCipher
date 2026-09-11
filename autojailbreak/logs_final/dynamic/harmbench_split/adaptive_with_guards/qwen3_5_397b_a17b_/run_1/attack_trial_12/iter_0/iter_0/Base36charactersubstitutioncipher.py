class Base36CharacterSubstitutionCipher:
    def __init__(self):
        plain = "0123456789abcdefghijklmnopqrstuvwxyz"
        cipher = "zyxwvutsrqponmlkjihgfedcba9876543210"
        self._enc = {p: c for p, c in zip(plain, cipher)}
        self._dec = {c: p for p, c in zip(plain, cipher)}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.islower() or ch.isdigit():
                out.append(self._enc.get(ch, ch))
            elif ch.isupper():
                mapped = self._enc.get(ch.lower(), ch.lower())
                out.append(mapped.upper() if mapped.isalpha() else mapped)
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch.islower() or ch.isdigit():
                out.append(self._dec.get(ch, ch))
            elif ch.isupper():
                mapped = self._dec.get(ch.lower(), ch.lower())
                out.append(mapped.upper() if mapped.isalpha() else mapped)
            else:
                out.append(ch)
        return "".join(out)
