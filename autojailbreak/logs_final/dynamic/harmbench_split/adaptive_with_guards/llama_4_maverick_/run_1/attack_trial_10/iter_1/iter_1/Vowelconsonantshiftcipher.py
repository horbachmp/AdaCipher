class VowelConsonantShiftCipher:
    def __init__(self):
        self.lower_vowel_enc = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
        self.upper_vowel_enc = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
        self.lower_vowel_dec = {'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o'}
        self.upper_vowel_dec = {'A': 'U', 'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O'}

        lower_consonants = "bcdfghjklmnpqrstvwxyz"
        lower_consonants_shifted = "cdfghjklmnpqrstvwxyzb"
        self.lower_cons_enc = dict(zip(lower_consonants, lower_consonants_shifted))
        self.lower_cons_dec = dict(zip(lower_consonants_shifted, lower_consonants))

        upper_consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        upper_consonants_shifted = "CDFGHJKLMNPQRSTVWXYZB"
        self.upper_cons_enc = dict(zip(upper_consonants, upper_consonants_shifted))
        self.upper_cons_dec = dict(zip(upper_consonants_shifted, upper_consonants))

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.lower_vowel_enc:
                result.append(self.lower_vowel_enc[ch])
            elif ch in self.upper_vowel_enc:
                result.append(self.upper_vowel_enc[ch])
            elif ch in self.lower_cons_enc:
                result.append(self.lower_cons_enc[ch])
            elif ch in self.upper_cons_enc:
                result.append(self.upper_cons_enc[ch])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.lower_vowel_dec:
                result.append(self.lower_vowel_dec[ch])
            elif ch in self.upper_vowel_dec:
                result.append(self.upper_vowel_dec[ch])
            elif ch in self.lower_cons_dec:
                result.append(self.lower_cons_dec[ch])
            elif ch in self.upper_cons_dec:
                result.append(self.upper_cons_dec[ch])
            else:
                result.append(ch)
        return "".join(result)
