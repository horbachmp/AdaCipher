class VowelConsonantInversionCipher:
    def __init__(self):
        self.vowels_lower = ['a', 'e', 'i', 'o', 'u']
        self.vowels_upper = ['A', 'E', 'I', 'O', 'U']
        self.consonants_lower = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        self.consonants_upper = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.vowels_lower:
                idx = self.vowels_lower.index(ch)
                result.append(self.vowels_lower[4 - idx])
            elif ch in self.vowels_upper:
                idx = self.vowels_upper.index(ch)
                result.append(self.vowels_upper[4 - idx])
            elif ch in self.consonants_lower:
                idx = self.consonants_lower.index(ch)
                result.append(self.consonants_lower[20 - idx])
            elif ch in self.consonants_upper:
                idx = self.consonants_upper.index(ch)
                result.append(self.consonants_upper[20 - idx])
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
