class VowelConsonantSplitShift:
    def __init__(self):
        self.vowels = "AEIOU"
        self.consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self.enc_vowel = {c: self.vowels[(i + 1) % len(self.vowels)] for i, c in enumerate(self.vowels)}
        self.dec_vowel = {c: self.vowels[(i - 1) % len(self.vowels)] for i, c in enumerate(self.vowels)}
        self.enc_cons = {c: self.consonants[(i + 1) % len(self.consonants)] for i, c in enumerate(self.consonants)}
        self.dec_cons = {c: self.consonants[(i - 1) % len(self.consonants)] for i, c in enumerate(self.consonants)}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.isalpha():
                upper = ch.upper()
                if upper in self.enc_vowel:
                    mapped = self.enc_vowel[upper]
                else:
                    mapped = self.enc_cons[upper]
                out.append(mapped if ch.isupper() else mapped.lower())
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch.isalpha():
                upper = ch.upper()
                if upper in self.dec_vowel:
                    mapped = self.dec_vowel[upper]
                else:
                    mapped = self.dec_cons[upper]
                out.append(mapped if ch.isupper() else mapped.lower())
            else:
                out.append(ch)
        return "".join(out)
