class Rot13WithVowelPreservation:
    def __init__(self):
        self.upper_vowels = set("AEIOU")
        self.lower_vowels = set("aeiou")
        self.upper_consonants = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if c not in self.upper_vowels]
        self.lower_consonants = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in self.lower_vowels]
        self.upper_map = {c: i for i, c in enumerate(self.upper_consonants)}
        self.lower_map = {c: i for i, c in enumerate(self.lower_consonants)}

    def _transform(self, text: str, shift: int) -> str:
        result = []
        for char in text:
            if char in self.upper_vowels or char in self.lower_vowels or not char.isalpha():
                result.append(char)
            elif char.isupper():
                idx = self.upper_map[char]
                result.append(self.upper_consonants[(idx + shift) % 21])
            else:
                idx = self.lower_map[char]
                result.append(self.lower_consonants[(idx + shift) % 21])
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext, 13)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext, 8)
