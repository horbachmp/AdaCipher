class VowelConsonantInterchangeCipher:
    def __init__(self):
        self.vowels = "AEIOU"
        self.consonants = "BCDFGHJKLMNPQRSTVWXYZ"

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if not char.isalpha():
                result.append(char)
                continue
            upper = char.upper()
            if upper in self.vowels:
                idx = self.vowels.index(upper)
                new_char = self.vowels[(idx + 2) % len(self.vowels)]
            else:
                idx = self.consonants.index(upper)
                new_char = self.consonants[(idx + 3) % len(self.consonants)]
            result.append(new_char if char.isupper() else new_char.lower())
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if not char.isalpha():
                result.append(char)
                continue
            upper = char.upper()
            if upper in self.vowels:
                idx = self.vowels.index(upper)
                new_char = self.vowels[(idx - 2) % len(self.vowels)]
            else:
                idx = self.consonants.index(upper)
                new_char = self.consonants[(idx - 3) % len(self.consonants)]
            result.append(new_char if char.isupper() else new_char.lower())
        return "".join(result)
