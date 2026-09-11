class Base36AlternateHomoglyph:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        self.size = len(self.alphabet)
        self.shift = 5

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            lower = ch.lower()
            if lower in self.alphabet:
                idx = self.alphabet.index(lower)
                result.append(self.alphabet[(idx + self.shift) % self.size])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            lower = ch.lower()
            if lower in self.alphabet:
                idx = self.alphabet.index(lower)
                result.append(self.alphabet[(idx - self.shift) % self.size])
            else:
                result.append(ch)
        return "".join(result)
