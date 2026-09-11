class VowelRotatorAndConsonantAtbash:
    def __init__(self):
        self._vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        mirrored = consonants[::-1]
        self._enc_map = {}
        self._dec_map = {}
        for c, m in zip(consonants, mirrored):
            self._enc_map[c] = m
            self._dec_map[m] = c
        for i, v in enumerate(self._vowels):
            self._enc_map[v] = self._vowels[(i + 1) % len(self._vowels)]
            self._dec_map[self._enc_map[v]] = v
        self._dec_vowel_map = {self._vowels[i]: self._vowels[(i - 1) % len(self._vowels)] for i in range(len(self._vowels))}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self._vowels:
                    mapped = self._enc_map[lower]
                else:
                    mapped = self._enc_map[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self._vowels:
                    mapped = self._dec_vowel_map[lower]
                else:
                    mapped = self._dec_map[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
