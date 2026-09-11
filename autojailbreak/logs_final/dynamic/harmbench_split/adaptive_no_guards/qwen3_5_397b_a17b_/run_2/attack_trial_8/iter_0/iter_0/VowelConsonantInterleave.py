class VowelConsonantInterleave:
    def __init__(self):
        self.upper_vowels = "AEIOU"
        self.lower_vowels = "aeiou"
        self.upper_consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self.lower_consonants = "bcdfghjklmnpqrstvwxyz"

    def _shift_char(self, char: str, direction: int) -> str:
        if not char.isalpha():
            return char
        if char in self.upper_vowels:
            seq = self.upper_vowels
            step = 2 * direction
        elif char in self.lower_vowels:
            seq = self.lower_vowels
            step = 2 * direction
        elif char in self.upper_consonants:
            seq = self.upper_consonants
            step = 5 * direction
        else:
            seq = self.lower_consonants
            step = 5 * direction
        idx = seq.index(char)
        return seq[(idx + step) % len(seq)]

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._shift_char(char, 1) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._shift_char(char, -1) for char in ciphertext)
