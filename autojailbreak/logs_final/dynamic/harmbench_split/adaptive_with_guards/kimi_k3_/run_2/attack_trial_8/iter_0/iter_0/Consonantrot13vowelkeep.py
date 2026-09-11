class ConsonantRot13VowelKeep:
    def __init__(self):
        self.upper = "BCDFGHJKLMNPQRSTVWXYZ"
        self.lower = "bcdfghjklmnpqrstvwxyz"
        self.shift = 11

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.upper:
                idx = self.upper.index(ch)
                result.append(self.upper[(idx + self.shift) % 21])
            elif ch in self.lower:
                idx = self.lower.index(ch)
                result.append(self.lower[(idx + self.shift) % 21])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.upper:
                idx = self.upper.index(ch)
                result.append(self.upper[(idx - self.shift) % 21])
            elif ch in self.lower:
                idx = self.lower.index(ch)
                result.append(self.lower[(idx - self.shift) % 21])
            else:
                result.append(ch)
        return "".join(result)
