class VowelConsonantShift:
    def __init__(self):
        self.vowel_next = {
            'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'
        }
        self.vowel_prev = {
            'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o'
        }
        self.consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        self.consonant_next = {}
        self.consonant_prev = {}
        n = len(self.consonants)
        for i, ch in enumerate(self.consonants):
            self.consonant_next[ch] = self.consonants[(i + 1) % n]
            self.consonant_prev[ch] = self.consonants[(i - 1) % n]

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            lower = char.lower()
            if lower.isalpha():
                if lower in self.vowel_next:
                    mapped = self.vowel_next[lower]
                else:
                    mapped = self.consonant_next[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            lower = char.lower()
            if lower.isalpha():
                if lower in self.vowel_prev:
                    mapped = self.vowel_prev[lower]
                else:
                    mapped = self.consonant_prev[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return "".join(result)
