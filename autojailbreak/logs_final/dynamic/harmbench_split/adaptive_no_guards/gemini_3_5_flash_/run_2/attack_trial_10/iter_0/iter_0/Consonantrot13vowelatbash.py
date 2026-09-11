class ConsonantRot13VowelAtbash:
    def __init__(self):
        self.vowel_map_upper = {'A': 'U', 'E': 'O', 'I': 'I', 'O': 'E', 'U': 'A'}
        self.vowel_map_lower = {'a': 'u', 'e': 'o', 'i': 'i', 'o': 'e', 'u': 'a'}
        self.consonants_upper = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        self.consonants_lower = [c.lower() for c in self.consonants_upper]
        self.enc_consonant_map_upper = {c: self.consonants_upper[(i + 10) % 21] for i, c in enumerate(self.consonants_upper)}
        self.enc_consonant_map_lower = {c: self.consonants_lower[(i + 10) % 21] for i, c in enumerate(self.consonants_lower)}
        self.dec_consonant_map_upper = {v: k for k, v in self.enc_consonant_map_upper.items()}
        self.dec_consonant_map_lower = {v: k for k, v in self.enc_consonant_map_lower.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.vowel_map_upper:
                result.append(self.vowel_map_upper[ch])
            elif ch in self.vowel_map_lower:
                result.append(self.vowel_map_lower[ch])
            elif ch in self.enc_consonant_map_upper:
                result.append(self.enc_consonant_map_upper[ch])
            elif ch in self.enc_consonant_map_lower:
                result.append(self.enc_consonant_map_lower[ch])
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.vowel_map_upper:
                result.append(self.vowel_map_upper[ch])
            elif ch in self.vowel_map_lower:
                result.append(self.vowel_map_lower[ch])
            elif ch in self.dec_consonant_map_upper:
                result.append(self.dec_consonant_map_upper[ch])
            elif ch in self.dec_consonant_map_lower:
                result.append(self.dec_consonant_map_lower[ch])
            else:
                result.append(ch)
        return ''.join(result)
