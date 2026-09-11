class Base36DigitAndVowelRotationCipher:
    def __init__(self):
        self._vowels_lower = "aeiou"
        self._vowels_upper = "AEIOU"
        self._enc_vowel_map = {
            "a": "e", "e": "i", "i": "o", "o": "u", "u": "a",
            "A": "E", "E": "I", "I": "O", "O": "U", "U": "A",
        }
        self._dec_vowel_map = {v: k for k, v in self._enc_vowel_map.items()}
        self._enc_digit_map = {str(i): str((i + 1) % 10) for i in range(10)}
        self._dec_digit_map = {v: k for k, v in self._enc_digit_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._enc_vowel_map:
                result.append(self._enc_vowel_map[ch])
            elif ch in self._enc_digit_map:
                result.append(self._enc_digit_map[ch])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._dec_vowel_map:
                result.append(self._dec_vowel_map[ch])
            elif ch in self._dec_digit_map:
                result.append(self._dec_digit_map[ch])
            else:
                result.append(ch)
        return "".join(result)
