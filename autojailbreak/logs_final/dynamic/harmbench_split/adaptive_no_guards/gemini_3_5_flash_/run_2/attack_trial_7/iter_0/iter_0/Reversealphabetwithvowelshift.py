class ReverseAlphabetWithVowelShift:
    def __init__(self):
        self.vowel_enc = {
            'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
            'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
        }
        self.vowel_dec = {v: k for k, v in self.vowel_enc.items()}
        consonants = "bcdfghjklmnpqrstvwxyz"
        reversed_consonants = "zyxwvtsrqpnmlkjhgfdbc"
        self.consonant_enc = {}
        self.consonant_dec = {}
        for a, b in zip(consonants, reversed_consonants):
            self.consonant_enc[a] = b
            self.consonant_enc[a.upper()] = b.upper()
            self.consonant_dec[b] = a
            self.consonant_dec[b.upper()] = a.upper()

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.vowel_enc:
                result.append(self.vowel_enc[ch])
            elif ch.lower() in self.consonant_enc:
                result.append(self.consonant_enc[ch.lower()].upper() if ch.isupper() else self.consonant_enc[ch.lower()])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.vowel_dec:
                result.append(self.vowel_dec[ch])
            elif ch.lower() in self.consonant_dec:
                result.append(self.consonant_dec[ch.lower()].upper() if ch.isupper() else self.consonant_dec[ch.lower()])
            else:
                result.append(ch)
        return "".join(result)
