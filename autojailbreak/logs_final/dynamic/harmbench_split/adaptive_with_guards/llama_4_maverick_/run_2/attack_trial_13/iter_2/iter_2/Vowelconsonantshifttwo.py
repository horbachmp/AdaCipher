class VowelConsonantShiftTwo:
    def __init__(self):
        self.vowel_enc = str.maketrans(
            "aeiouAEIOU",
            "eiouaEIOUA",
        )
        self.vowel_dec = str.maketrans(
            "eiouaEIOUA",
            "aeiouAEIOU",
        )
        self.consonants_lower = "bcdfghjklmnpqrstvwxyz"
        self.consonants_upper = self.consonants_lower.upper()
        self.consonant_enc = {c: self.consonants_lower[(i + 1) % len(self.consonants_lower)] for i, c in enumerate(self.consonants_lower)}
        self.consonant_dec = {c: self.consonants_lower[(i - 1) % len(self.consonants_lower)] for i, c in enumerate(self.consonants_lower)}
        self.consonant_enc.update({c.upper(): self.consonant_enc[c].upper() for c in self.consonants_lower})
        self.consonant_dec.update({c.upper(): self.consonant_dec[c].upper() for c in self.consonants_lower})

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in "aeiouAEIOU":
                result.append(ch.translate(self.vowel_enc))
            elif ch.isalpha():
                result.append(self.consonant_enc.get(ch, ch))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in "aeiouAEIOU":
                result.append(ch.translate(self.vowel_dec))
            elif ch.isalpha():
                result.append(self.consonant_dec.get(ch, ch))
            else:
                result.append(ch)
        return "".join(result)
