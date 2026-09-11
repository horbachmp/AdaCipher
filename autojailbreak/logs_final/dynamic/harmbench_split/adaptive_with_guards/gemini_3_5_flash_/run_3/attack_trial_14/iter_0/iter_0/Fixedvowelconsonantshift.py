class FixedVowelConsonantShift:
    def __init__(self):
        self._vowels = "AEIOU"
        self._consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self._enc_vowel = {self._vowels[i]: self._vowels[(i + 1) % len(self._vowels)] for i in range(len(self._vowels))}
        self._dec_vowel = {self._vowels[i]: self._vowels[(i - 1) % len(self._vowels)] for i in range(len(self._vowels))}
        self._enc_cons = {self._consonants[i]: self._consonants[(i + 1) % len(self._consonants)] for i in range(len(self._consonants))}
        self._dec_cons = {self._consonants[i]: self._consonants[(i - 1) % len(self._consonants)] for i in range(len(self._consonants))}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                upper = ch.upper()
                if upper in self._enc_vowel:
                    mapped = self._enc_vowel[upper]
                else:
                    mapped = self._enc_cons[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                upper = ch.upper()
                if upper in self._dec_vowel:
                    mapped = self._dec_vowel[upper]
                else:
                    mapped = self._dec_cons[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)
