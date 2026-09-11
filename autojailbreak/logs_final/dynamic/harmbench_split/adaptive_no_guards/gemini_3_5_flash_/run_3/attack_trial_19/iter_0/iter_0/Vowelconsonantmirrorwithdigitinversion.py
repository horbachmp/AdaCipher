class VowelConsonantMirrorWithDigitInversion:
    def __init__(self):
        self.vowel_map = {
            'a': 'u', 'e': 'o', 'i': 'i', 'o': 'e', 'u': 'a',
            'A': 'U', 'E': 'O', 'I': 'I', 'O': 'E', 'U': 'A',
        }
        self.consonant_map = {
            'b': 'z', 'c': 'y', 'd': 'x', 'f': 'w', 'g': 'v', 'h': 't',
            'j': 's', 'k': 'r', 'l': 'q', 'm': 'p', 'n': 'n',
            'p': 'm', 'q': 'l', 'r': 'k', 's': 'j', 't': 'h', 'v': 'g',
            'w': 'f', 'x': 'd', 'y': 'c', 'z': 'b',
            'B': 'Z', 'C': 'Y', 'D': 'X', 'F': 'W', 'G': 'V', 'H': 'T',
            'J': 'S', 'K': 'R', 'L': 'Q', 'M': 'P', 'N': 'N',
            'P': 'M', 'Q': 'L', 'R': 'K', 'S': 'J', 'T': 'H', 'V': 'G',
            'W': 'F', 'X': 'D', 'Y': 'C', 'Z': 'B',
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char in self.vowel_map:
                result.append(self.vowel_map[char])
            elif char in self.consonant_map:
                result.append(self.consonant_map[char])
            elif char.isdigit():
                result.append(str(9 - int(char)))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
