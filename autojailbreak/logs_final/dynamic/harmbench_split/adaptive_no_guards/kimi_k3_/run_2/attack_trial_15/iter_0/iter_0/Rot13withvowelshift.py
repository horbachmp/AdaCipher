class Rot13WithVowelShift:
    def __init__(self):
        self._upper_vowels = "AEIOU"
        self._lower_vowels = "aeiou"

    def _rot13(self, char: str) -> str:
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        if 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        return char

    def _next_vowel(self, char: str) -> str:
        if char in self._upper_vowels:
            idx = self._upper_vowels.index(char)
            return self._upper_vowels[(idx + 1) % 5]
        if char in self._lower_vowels:
            idx = self._lower_vowels.index(char)
            return self._lower_vowels[(idx + 1) % 5]
        return char

    def _prev_vowel(self, char: str) -> str:
        if char in self._upper_vowels:
            idx = self._upper_vowels.index(char)
            return self._upper_vowels[(idx - 1) % 5]
        if char in self._lower_vowels:
            idx = self._lower_vowels.index(char)
            return self._lower_vowels[(idx - 1) % 5]
        return char

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                ch = self._rot13(char)
                ch = self._next_vowel(ch)
                result.append(ch)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char.isalpha():
                ch = self._prev_vowel(char) if char in self._upper_vowels + self._lower_vowels else char
                ch = self._rot13(ch)
                result.append(ch)
            else:
                result.append(char)
        return "".join(result)
