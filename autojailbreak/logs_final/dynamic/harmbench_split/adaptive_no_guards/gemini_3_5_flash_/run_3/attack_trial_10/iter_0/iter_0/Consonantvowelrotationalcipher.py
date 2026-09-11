class ConsonantVowelRotationalCipher:
    def __init__(self):
        self.lower_vowels = ['a', 'e', 'i', 'o', 'u']
        self.upper_vowels = ['A', 'E', 'I', 'O', 'U']
        self.lower_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        self.upper_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char in self.lower_vowels:
                idx = self.lower_vowels.index(char)
                result.append(self.lower_vowels[(idx + 2) % 5])
            elif char in self.upper_vowels:
                idx = self.upper_vowels.index(char)
                result.append(self.upper_vowels[(idx + 2) % 5])
            elif char in self.lower_consonants:
                idx = self.lower_consonants.index(char)
                result.append(self.lower_consonants[(idx + 5) % 21])
            elif char in self.upper_consonants:
                idx = self.upper_consonants.index(char)
                result.append(self.upper_consonants[(idx + 5) % 21])
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char in self.lower_vowels:
                idx = self.lower_vowels.index(char)
                result.append(self.lower_vowels[(idx - 2) % 5])
            elif char in self.upper_vowels:
                idx = self.upper_vowels.index(char)
                result.append(self.upper_vowels[(idx - 2) % 5])
            elif char in self.lower_consonants:
                idx = self.lower_consonants.index(char)
                result.append(self.lower_consonants[(idx - 5) % 21])
            elif char in self.upper_consonants:
                idx = self.upper_consonants.index(char)
                result.append(self.upper_consonants[(idx - 5) % 21])
            else:
                result.append(char)
        return ''.join(result)
