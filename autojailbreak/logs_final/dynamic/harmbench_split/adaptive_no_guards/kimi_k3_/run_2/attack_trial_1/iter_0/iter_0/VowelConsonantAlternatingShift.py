class VowelConsonantAlternatingShift:
    def __init__(self):
        self.vowels = "aeiou"
        self.consonants = "bcdfghjklmnpqrstvwxyz"
        self.enc_vowel = {self.vowels[i]: self.vowels[(i + 1) % len(self.vowels)] for i in range(len(self.vowels))}
        self.dec_vowel = {self.vowels[i]: self.vowels[(i - 1) % len(self.vowels)] for i in range(len(self.vowels))}
        self.enc_cons = {self.consonants[i]: self.consonants[(i + 1) % len(self.consonants)] for i in range(len(self.consonants))}
        self.dec_cons = {self.consonants[i]: self.consonants[(i - 1) % len(self.consonants)] for i in range(len(self.consonants))}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            lower = ch.lower()
            if lower in self.enc_vowel:
                mapped = self.enc_vowel[lower]
                out.append(mapped.upper() if ch.isupper() else mapped)
            elif lower in self.enc_cons:
                mapped = self.enc_cons[lower]
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            lower = ch.lower()
            if lower in self.dec_vowel:
                mapped = self.dec_vowel[lower]
                out.append(mapped.upper() if ch.isupper() else mapped)
            elif lower in self.dec_cons:
                mapped = self.dec_cons[lower]
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)
