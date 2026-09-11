class ReverseAlphabetWithVowelPreservation:
    def __init__(self):
        self.vowels_lower = set("aeiou")
        self.vowels_upper = set("AEIOU")
        consonants = "bcdfghjklmnpqrstvwxyz"
        reversed_consonants = consonants[::-1]
        self.lower_enc = {c: r for c, r in zip(consonants, reversed_consonants)}
        self.lower_dec = {r: c for c, r in zip(consonants, reversed_consonants)}
        self.upper_enc = {c.upper(): r.upper() for c, r in zip(consonants, reversed_consonants)}
        self.upper_dec = {r.upper(): c.upper() for c, r in zip(consonants, reversed_consonants)}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if not ch.isalpha():
                out.append(ch)
            elif ch in self.vowels_lower or ch in self.vowels_upper:
                out.append(ch)
            elif ch.islower():
                out.append(self.lower_enc[ch])
            else:
                out.append(self.upper_enc[ch])
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if not ch.isalpha():
                out.append(ch)
            elif ch in self.vowels_lower or ch in self.vowels_upper:
                out.append(ch)
            elif ch.islower():
                out.append(self.lower_dec[ch])
            else:
                out.append(self.upper_dec[ch])
        return "".join(out)
