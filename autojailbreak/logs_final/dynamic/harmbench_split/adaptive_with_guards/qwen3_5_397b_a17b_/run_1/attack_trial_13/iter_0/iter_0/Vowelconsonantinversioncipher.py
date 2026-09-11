class VowelConsonantInversionCipher:
    def __init__(self):
        self.vowel_map = {
            "a": "u",
            "e": "o",
            "i": "i",
            "o": "e",
            "u": "a",
        }
        consonants = "bcdfghjklmnpqrstvwxyz"
        reversed_consonants = consonants[::-1]
        self.consonant_map = {c: r for c, r in zip(consonants, reversed_consonants)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            lower = char.lower()
            if lower in self.vowel_map:
                mapped = self.vowel_map[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            elif char.isalpha():
                mapped = self.consonant_map[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
