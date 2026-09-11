class VowelShiftConsonantRot5:
    def __init__(self):
        self.vowels = "aeiou"
        self.consonants = "bcdfghjklmnpqrstvwxyz"
        self.vowel_map_enc = {self.vowels[i]: self.vowels[(i + 1) % 5] for i in range(5)}
        self.vowel_map_dec = {self.vowels[i]: self.vowels[(i - 1) % 5] for i in range(5)}
        self.consonant_map_enc = {c: self.consonants[(i + 5) % 21] for i, c in enumerate(self.consonants)}
        self.consonant_map_dec = {c: self.consonants[(i - 5) % 21] for i, c in enumerate(self.consonants)}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.isalpha():
                low = ch.lower()
                if low in self.vowel_map_enc:
                    mapped = self.vowel_map_enc[low]
                else:
                    mapped = self.consonant_map_enc[low]
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch.isalpha():
                low = ch.lower()
                if low in self.vowel_map_dec:
                    mapped = self.vowel_map_dec[low]
                else:
                    mapped = self.consonant_map_dec[low]
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)
