class VowelConsonantShift:
    def __init__(self):
        self.vowel_enc = {
            'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
            'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
        }
        self.vowel_dec = {
            'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o', 'a': 'u',
            'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O', 'A': 'U'
        }
        self.consonant_enc = {
            'b': 'c', 'c': 'd', 'd': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'j': 'k',
            'k': 'l', 'l': 'm', 'm': 'n', 'n': 'p', 'p': 'q', 'q': 'r', 'r': 's',
            's': 't', 't': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'b',
            'B': 'C', 'C': 'D', 'D': 'F', 'F': 'G', 'G': 'H', 'H': 'J', 'J': 'K',
            'K': 'L', 'L': 'M', 'M': 'N', 'N': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S',
            'S': 'T', 'T': 'V', 'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'B'
        }
        self.consonant_dec = {
            'c': 'b', 'd': 'c', 'f': 'd', 'g': 'f', 'h': 'g', 'j': 'h', 'k': 'j',
            'l': 'k', 'm': 'l', 'n': 'm', 'p': 'n', 'q': 'p', 'r': 'q', 's': 'r',
            't': 's', 'v': 't', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y', 'b': 'z',
            'C': 'B', 'D': 'C', 'F': 'D', 'G': 'F', 'H': 'G', 'J': 'H', 'K': 'J',
            'L': 'K', 'M': 'L', 'N': 'M', 'P': 'N', 'Q': 'P', 'R': 'Q', 'S': 'R',
            'T': 'S', 'V': 'T', 'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Y', 'B': 'Z'
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char in self.vowel_enc:
                result.append(self.vowel_enc[char])
            elif char in self.consonant_enc:
                result.append(self.consonant_enc[char])
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char in self.vowel_dec:
                result.append(self.vowel_dec[char])
            elif char in self.consonant_dec:
                result.append(self.consonant_dec[char])
            else:
                result.append(char)
        return ''.join(result)
