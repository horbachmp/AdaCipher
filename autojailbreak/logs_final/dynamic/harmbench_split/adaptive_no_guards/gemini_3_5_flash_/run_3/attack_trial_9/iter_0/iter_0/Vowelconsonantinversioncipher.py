class VowelConsonantInversionCipher:
    def __init__(self):
        vowels = "AEIOU"
        consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        reversed_vowels = vowels[::-1]
        reversed_consonants = consonants[::-1]
        self._enc = {}
        for a, b in zip(vowels, reversed_vowels):
            self._enc[a] = b
        for a, b in zip(consonants, reversed_consonants):
            self._enc[a] = b
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                upper = ch.upper()
                mapped = self._enc.get(upper, upper)
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                upper = ch.upper()
                mapped = self._dec.get(upper, upper)
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)
