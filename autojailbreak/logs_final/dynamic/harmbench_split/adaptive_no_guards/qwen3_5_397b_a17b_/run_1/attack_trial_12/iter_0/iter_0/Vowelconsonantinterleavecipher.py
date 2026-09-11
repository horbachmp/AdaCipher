class VowelConsonantInterleaveCipher:
    def __init__(self):
        self.vowels = "aeiou"
        self.consonants = "bcdfghjklmnpqrstvwxyz"

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if not ch.isalpha():
                result.append(ch)
                continue
            lower = ch.lower()
            if lower in self.vowels:
                idx = self.vowels.index(lower)
                mapped = self.vowels[(idx + 1) % 5]
            else:
                idx = self.consonants.index(lower)
                mapped = self.consonants[(idx + 2) % 21]
            result.append(mapped.upper() if ch.isupper() else mapped)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if not ch.isalpha():
                result.append(ch)
                continue
            lower = ch.lower()
            if lower in self.vowels:
                idx = self.vowels.index(lower)
                mapped = self.vowels[(idx - 1) % 5]
            else:
                idx = self.consonants.index(lower)
                mapped = self.consonants[(idx - 2) % 21]
            result.append(mapped.upper() if ch.isupper() else mapped)
        return "".join(result)
