class VowelConsonantSplitCipher:
    def __init__(self):
        self.vowels_upper = "AEIOU"
        self.vowels_lower = "aeiou"
        self.consonants_upper = "BCDFGHJKLMNPQRSTVWXYZ"
        self.consonants_lower = "bcdfghjklmnpqrstvwxyz"

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.vowels_upper:
                idx = self.vowels_upper.index(ch)
                result.append(self.vowels_upper[(idx + 1) % len(self.vowels_upper)])
            elif ch in self.vowels_lower:
                idx = self.vowels_lower.index(ch)
                result.append(self.vowels_lower[(idx + 1) % len(self.vowels_lower)])
            elif ch in self.consonants_upper:
                idx = self.consonants_upper.index(ch)
                result.append(self.consonants_upper[(idx + 1) % len(self.consonants_upper)])
            elif ch in self.consonants_lower:
                idx = self.consonants_lower.index(ch)
                result.append(self.consonants_lower[(idx + 1) % len(self.consonants_lower)])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.vowels_upper:
                idx = self.vowels_upper.index(ch)
                result.append(self.vowels_upper[(idx - 1) % len(self.vowels_upper)])
            elif ch in self.vowels_lower:
                idx = self.vowels_lower.index(ch)
                result.append(self.vowels_lower[(idx - 1) % len(self.vowels_lower)])
            elif ch in self.consonants_upper:
                idx = self.consonants_upper.index(ch)
                result.append(self.consonants_upper[(idx - 1) % len(self.consonants_upper)])
            elif ch in self.consonants_lower:
                idx = self.consonants_lower.index(ch)
                result.append(self.consonants_lower[(idx - 1) % len(self.consonants_lower)])
            else:
                result.append(ch)
        return "".join(result)
