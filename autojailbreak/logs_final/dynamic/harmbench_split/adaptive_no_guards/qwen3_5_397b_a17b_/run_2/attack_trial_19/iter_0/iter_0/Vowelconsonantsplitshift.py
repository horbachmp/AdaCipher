class VowelConsonantSplitShift:
    def __init__(self):
        self.vowels = "AEIOU"
        self.consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self.enc_vowel = {self.vowels[i]: self.vowels[(i - 1) % 5] for i in range(5)}
        self.dec_vowel = {self.vowels[i]: self.vowels[(i + 1) % 5] for i in range(5)}
        self.enc_cons = {self.consonants[i]: self.consonants[(i + 2) % 21] for i in range(21)}
        self.dec_cons = {self.consonants[i]: self.consonants[(i - 2) % 21] for i in range(21)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            upper = ch.upper()
            if upper in self.enc_vowel:
                mapped = self.enc_vowel[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            elif upper in self.enc_cons:
                mapped = self.enc_cons[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            upper = ch.upper()
            if upper in self.dec_vowel:
                mapped = self.dec_vowel[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            elif upper in self.dec_cons:
                mapped = self.dec_cons[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)
