class AlternatingCaseVowelConsonantShift:
    def __init__(self):
        self.vowels = "AEIOU"
        self.consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self.vowel_next = {self.vowels[i]: self.vowels[(i + 1) % len(self.vowels)] for i in range(len(self.vowels))}
        self.vowel_prev = {self.vowels[i]: self.vowels[(i - 1) % len(self.vowels)] for i in range(len(self.vowels))}
        self.consonant_next = {self.consonants[i]: self.consonants[(i + 1) % len(self.consonants)] for i in range(len(self.consonants))}
        self.consonant_prev = {self.consonants[i]: self.consonants[(i - 1) % len(self.consonants)] for i in range(len(self.consonants))}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            up = ch.upper()
            if up in self.vowel_next:
                new_ch = self.vowel_next[up]
                out.append(new_ch if ch.isupper() else new_ch.lower())
            elif up in self.consonant_next:
                new_ch = self.consonant_next[up]
                out.append(new_ch if ch.isupper() else new_ch.lower())
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            up = ch.upper()
            if up in self.vowel_prev:
                new_ch = self.vowel_prev[up]
                out.append(new_ch if ch.isupper() else new_ch.lower())
            elif up in self.consonant_prev:
                new_ch = self.consonant_prev[up]
                out.append(new_ch if ch.isupper() else new_ch.lower())
            else:
                out.append(ch)
        return "".join(out)
