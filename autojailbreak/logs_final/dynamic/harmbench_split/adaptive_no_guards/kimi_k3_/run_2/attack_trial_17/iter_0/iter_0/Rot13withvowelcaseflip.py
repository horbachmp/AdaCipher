class Rot13WithVowelCaseFlip:
    def __init__(self):
        pass

    @staticmethod
    def _rot13_char(char: str) -> str:
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        if 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        return char

    @staticmethod
    def _is_vowel(char: str) -> bool:
        return char in "AEIOUaeiou"

    @staticmethod
    def _flip_case(char: str) -> str:
        if char.islower():
            return char.upper()
        if char.isupper():
            return char.lower()
        return char

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            transformed = self._rot13_char(char)
            if self._is_vowel(transformed):
                transformed = self._flip_case(transformed)
            result.append(transformed)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            transformed = char
            if self._is_vowel(transformed):
                transformed = self._flip_case(transformed)
            transformed = self._rot13_char(transformed)
            result.append(transformed)
        return "".join(result)
