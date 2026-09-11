class VowelConsonantIndexShiftCipher:
    def __init__(self):
        self._vowels_lower = "aeiou"
        self._vowels_upper = "AEIOU"
        self._consonants_lower = "bcdfghjklmnpqrstvwxyz"
        self._consonants_upper = "BCDFGHJKLMNPQRSTVWXYZ"
        self._enc_vowel = {self._vowels_lower[i]: self._vowels_lower[(i + 1) % 5] for i in range(5)}
        self._dec_vowel = {self._vowels_lower[i]: self._vowels_lower[(i - 1) % 5] for i in range(5)}
        self._enc_cons = {self._consonants_lower[i]: self._consonants_lower[(i + 1) % 21] for i in range(21)}
        self._dec_cons = {self._consonants_lower[i]: self._consonants_lower[(i - 1) % 21] for i in range(21)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._vowels_lower:
                result.append(self._enc_vowel[ch])
            elif ch in self._vowels_upper:
                result.append(self._enc_vowel[ch.lower()].upper())
            elif ch in self._consonants_lower:
                result.append(self._enc_cons[ch])
            elif ch in self._consonants_upper:
                result.append(self._enc_cons[ch.lower()].upper())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._vowels_lower:
                result.append(self._dec_vowel[ch])
            elif ch in self._vowels_upper:
                result.append(self._dec_vowel[ch.lower()].upper())
            elif ch in self._consonants_lower:
                result.append(self._dec_cons[ch])
            elif ch in self._consonants_upper:
                result.append(self._dec_cons[ch.lower()].upper())
            else:
                result.append(ch)
        return "".join(result)
