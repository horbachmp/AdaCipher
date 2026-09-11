class FixedVowelConsonantInversion:
    def __init__(self):
        self.vowel_map = {
            'A': 'U', 'E': 'O', 'I': 'I', 'O': 'E', 'U': 'A',
            'a': 'u', 'e': 'o', 'i': 'i', 'o': 'e', 'u': 'a'
        }
        self.consonant_map = {
            'B': 'Z', 'C': 'Y', 'D': 'X', 'F': 'W', 'G': 'V', 'H': 'T',
            'J': 'S', 'K': 'R', 'L': 'Q', 'M': 'P', 'N': 'N',
            'b': 'z', 'c': 'y', 'd': 'x', 'f': 'w', 'g': 'v', 'h': 't',
            'j': 's', 'k': 'r', 'l': 'q', 'm': 'p', 'n': 'n'
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char in self.vowel_map:
                result.append(self.vowel_map[char])
            elif char in self.consonant_map:
                result.append(self.consonant_map[char])
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char in self.vowel_map:
                result.append(self.vowel_map[char])
            elif char in self.consonant_map:
                result.append(self.consonant_map[char])
            else:
                result.append(char)
        return ''.join(result)
