class VowelLeetConsonantRot13:
    def __init__(self):
        self._vowel_to_digit = {
            "a": "4",
            "e": "3",
            "i": "1",
            "o": "0",
            "u": "5",
        }
        self._digit_to_vowel = {v: k for k, v in self._vowel_to_digit.items()}
        self._consonants_lower = "bcdfghjklmnpqrstvwxyz"
        self._consonants_upper = self._consonants_lower.upper()

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self._vowel_to_digit:
                    result.append(self._vowel_to_digit[lower])
                else:
                    alphabet = self._consonants_upper if ch.isupper() else self._consonants_lower
                    idx = alphabet.index(ch)
                    result.append(alphabet[(idx + 13) % 21])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._digit_to_vowel:
                result.append(self._digit_to_vowel[ch])
            elif ch.isalpha():
                alphabet = self._consonants_upper if ch.isupper() else self._consonants_lower
                idx = alphabet.index(ch)
                result.append(alphabet[(idx - 13) % 21])
            else:
                result.append(ch)
        return "".join(result)
