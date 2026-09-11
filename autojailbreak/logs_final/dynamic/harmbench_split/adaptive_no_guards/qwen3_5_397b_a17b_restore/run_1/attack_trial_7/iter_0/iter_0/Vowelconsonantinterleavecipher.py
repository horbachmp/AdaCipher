class VowelConsonantInterleaveCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def encrypt(self, plaintext: str) -> str:
        letters = [c for c in plaintext if c.isalpha()]
        vowels = [c for c in letters if c in self.vowels]
        consonants = [c for c in letters if c not in self.vowels]
        combined = iter(vowels + consonants)
        result = []
        for c in plaintext:
            if c.isalpha():
                result.append(next(combined))
            else:
                result.append(c)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        letter_positions = [i for i, c in enumerate(ciphertext) if c.isalpha()]
        letters = [ciphertext[i] for i in letter_positions]
        vowel_count = sum(1 for c in letters if c in self.vowels)
        vowels = letters[:vowel_count]
        consonants = letters[vowel_count:]
        v_idx = 0
        c_idx = 0
        result = list(ciphertext)
        for i, c in enumerate(result):
            if c.isalpha():
                if c in self.vowels:
                    result[i] = vowels[v_idx]
                    v_idx += 1
                else:
                    result[i] = consonants[c_idx]
                    c_idx += 1
        return "".join(result)
