class VowelConsonantShiftOneCipher:
    def __init__(self):
        self.lower_vowels = ['a', 'e', 'i', 'o', 'u']
        self.upper_vowels = ['A', 'E', 'I', 'O', 'U']
        self.lower_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        self.upper_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        self.lower_vowel_map = {c: self.lower_vowels[(i + 1) % len(self.lower_vowels)] for i, c in enumerate(self.lower_vowels)}
        self.upper_vowel_map = {c: self.upper_vowels[(i + 1) % len(self.upper_vowels)] for i, c in enumerate(self.upper_vowels)}
        self.lower_consonant_map = {c: self.lower_consonants[(i + 1) % len(self.lower_consonants)] for i, c in enumerate(self.lower_consonants)}
        self.upper_consonant_map = {c: self.upper_consonants[(i + 1) % len(self.upper_consonants)] for i, c in enumerate(self.upper_consonants)}
        self.lower_vowel_unmap = {v: k for k, v in self.lower_vowel_map.items()}
        self.upper_vowel_unmap = {v: k for k, v in self.upper_vowel_map.items()}
        self.lower_consonant_unmap = {v: k for k, v in self.lower_consonant_map.items()}
        self.upper_consonant_unmap = {v: k for k, v in self.upper_consonant_map.items()}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch in self.lower_vowel_map:
                out.append(self.lower_vowel_map[ch])
            elif ch in self.upper_vowel_map:
                out.append(self.upper_vowel_map[ch])
            elif ch in self.lower_consonant_map:
                out.append(self.lower_consonant_map[ch])
            elif ch in self.upper_consonant_map:
                out.append(self.upper_consonant_map[ch])
            else:
                out.append(ch)
        return ''.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch in self.lower_vowel_unmap:
                out.append(self.lower_vowel_unmap[ch])
            elif ch in self.upper_vowel_unmap:
                out.append(self.upper_vowel_unmap[ch])
            elif ch in self.lower_consonant_unmap:
                out.append(self.lower_consonant_unmap[ch])
            elif ch in self.upper_consonant_unmap:
                out.append(self.upper_consonant_unmap[ch])
            else:
                out.append(ch)
        return ''.join(out)
