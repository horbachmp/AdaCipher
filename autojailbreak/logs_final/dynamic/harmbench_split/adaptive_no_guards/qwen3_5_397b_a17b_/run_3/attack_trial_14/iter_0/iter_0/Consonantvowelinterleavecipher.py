class ConsonantVowelInterleaveCipher:
    def __init__(self):
        self._vowels_lower = "aeiou"
        self._vowel_enc = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"}
        self._vowel_dec = {"e": "a", "i": "e", "o": "i", "u": "o", "a": "u"}

        consonants = "bcdfghjklmnpqrstvwxyz"
        self._cons_enc = {consonants[i]: consonants[(i + 1) % len(consonants)] for i in range(len(consonants))}
        self._cons_dec = {v: k for k, v in self._cons_enc.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self._vowel_enc:
                    mapped = self._vowel_enc[lower]
                else:
                    mapped = self._cons_enc[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self._vowel_dec:
                    mapped = self._vowel_dec[lower]
                else:
                    mapped = self._cons_dec[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
