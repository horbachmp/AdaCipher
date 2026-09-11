class VowelConsonantShiftCipher:
    def __init__(self):
        self.vowel_enc = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
        self.vowel_dec = {'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O', 'A': 'U'}
        self.consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        self.consonant_enc = {self.consonants[i]: self.consonants[(i + 1) % len(self.consonants)] for i in range(len(self.consonants))}
        self.consonant_dec = {self.consonants[i]: self.consonants[(i - 1) % len(self.consonants)] for i in range(len(self.consonants))}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            upper = ch.upper()
            if upper in self.vowel_enc:
                mapped = self.vowel_enc[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            elif upper in self.consonant_enc:
                mapped = self.consonant_enc[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            upper = ch.upper()
            if upper in self.vowel_dec:
                mapped = self.vowel_dec[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            elif upper in self.consonant_dec:
                mapped = self.consonant_dec[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return ''.join(result)
