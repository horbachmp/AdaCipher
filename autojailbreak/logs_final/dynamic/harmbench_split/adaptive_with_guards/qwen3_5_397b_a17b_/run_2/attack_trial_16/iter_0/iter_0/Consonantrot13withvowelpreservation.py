class ConsonantRot13WithVowelPreservation:
    def __init__(self):
        self.lower = "bcdfghjklmnpqrstvwxyz"
        self.upper = "BCDFGHJKLMNPQRSTVWXYZ"
        self.shift = 13
        self.vowels = set("aeiouAEIOU")

    def _transform(self, text: str) -> str:
        result = []
        for ch in text:
            if ch in self.vowels:
                result.append(ch)
            elif ch in self.lower:
                idx = self.lower.index(ch)
                result.append(self.lower[(idx + self.shift) % len(self.lower)])
            elif ch in self.upper:
                idx = self.upper.index(ch)
                result.append(self.upper[(idx + self.shift) % len(self.upper)])
            else:
                result.append(ch)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
