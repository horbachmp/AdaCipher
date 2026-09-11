class VowelConsonantAlternatingShift:
    def __init__(self):
        self.lower_vowels = "aeiou"
        self.upper_vowels = "AEIOU"
        self.lower_consonants = "bcdfghjklmnpqrstvwxyz"
        self.upper_consonants = "BCDFGHJKLMNPQRSTVWXYZ"

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.lower_vowels:
                idx = self.lower_vowels.index(ch)
                result.append(self.lower_vowels[(idx + 1) % len(self.lower_vowels)])
            elif ch in self.upper_vowels:
                idx = self.upper_vowels.index(ch)
                result.append(self.upper_vowels[(idx + 1) % len(self.upper_vowels)])
            elif ch in self.lower_consonants:
                idx = self.lower_consonants.index(ch)
                result.append(self.lower_consonants[(idx + 1) % len(self.lower_consonants)])
            elif ch in self.upper_consonants:
                idx = self.upper_consonants.index(ch)
                result.append(self.upper_consonants[(idx + 1) % len(self.upper_consonants)])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.lower_vowels:
                idx = self.lower_vowels.index(ch)
                result.append(self.lower_vowels[(idx - 1) % len(self.lower_vowels)])
            elif ch in self.upper_vowels:
                idx = self.upper_vowels.index(ch)
                result.append(self.upper_vowels[(idx - 1) % len(self.upper_vowels)])
            elif ch in self.lower_consonants:
                idx = self.lower_consonants.index(ch)
                result.append(self.lower_consonants[(idx - 1) % len(self.lower_consonants)])
            elif ch in self.upper_consonants:
                idx = self.upper_consonants.index(ch)
                result.append(self.upper_consonants[(idx - 1) % len(self.upper_consonants)])
            else:
                result.append(ch)
        return "".join(result)
