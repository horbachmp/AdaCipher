class ConsonantVowelInterleaveCipher:
    def __init__(self):
        self.vowels = "aeiou"
        self.consonants = "bcdfghjklmnpqrstvwxyz"
        self.vowel_enc = {v: self.vowels[(i + 1) % len(self.vowels)] for i, v in enumerate(self.vowels)}
        self.vowel_dec = {v: self.vowels[(i - 1) % len(self.vowels)] for i, v in enumerate(self.vowels)}
        self.cons_enc = {c: self.consonants[(i + 1) % len(self.consonants)] for i, c in enumerate(self.consonants)}
        self.cons_dec = {c: self.consonants[(i - 1) % len(self.consonants)] for i, c in enumerate(self.consonants)}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            low = ch.lower()
            if low in self.vowel_enc:
                enc = self.vowel_enc[low]
                out.append(enc.upper() if ch.isupper() else enc)
            elif low in self.cons_enc:
                enc = self.cons_enc[low]
                out.append(enc.upper() if ch.isupper() else enc)
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            low = ch.lower()
            if low in self.vowel_dec:
                dec = self.vowel_dec[low]
                out.append(dec.upper() if ch.isupper() else dec)
            elif low in self.cons_dec:
                dec = self.cons_dec[low]
                out.append(dec.upper() if ch.isupper() else dec)
            else:
                out.append(ch)
        return "".join(out)
