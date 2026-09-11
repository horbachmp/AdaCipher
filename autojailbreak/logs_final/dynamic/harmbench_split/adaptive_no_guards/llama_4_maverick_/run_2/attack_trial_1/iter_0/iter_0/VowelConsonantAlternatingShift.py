class VowelConsonantAlternatingShift:
    def __init__(self):
        self.vowels = "aeiou"
        self.consonants = "bcdfghjklmnpqrstvwxyz"
        self.vowel_next = {self.vowels[i]: self.vowels[(i + 1) % len(self.vowels)] for i in range(len(self.vowels))}
        self.vowel_prev = {self.vowels[i]: self.vowels[(i - 1) % len(self.vowels)] for i in range(len(self.vowels))}
        self.cons_next = {self.consonants[i]: self.consonants[(i + 1) % len(self.consonants)] for i in range(len(self.consonants))}
        self.cons_prev = {self.consonants[i]: self.consonants[(i - 1) % len(self.consonants)] for i in range(len(self.consonants))}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self.vowel_next:
                    mapped = self.vowel_next[lower]
                else:
                    mapped = self.cons_next[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self.vowel_prev:
                    mapped = self.vowel_prev[lower]
                else:
                    mapped = self.cons_prev[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
