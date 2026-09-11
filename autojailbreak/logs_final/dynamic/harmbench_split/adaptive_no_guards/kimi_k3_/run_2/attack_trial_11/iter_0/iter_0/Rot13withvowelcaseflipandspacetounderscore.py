class Rot13WithVowelCaseFlipAndSpaceToUnderscore:
    def __init__(self):
        pass

    def _rot13_char(self, char: str) -> str:
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        if 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        return char

    def _flip_case(self, char: str) -> str:
        if char.islower():
            return char.upper()
        if char.isupper():
            return char.lower()
        return char

    def encrypt(self, plaintext: str) -> str:
        result = []
        vowels = set("AEIOUaeiou")
        for char in plaintext:
            if char == ' ':
                result.append('_')
            elif char == '_':
                result.append(' ')
            elif char.isalpha():
                c = self._rot13_char(char)
                if c in vowels:
                    c = self._flip_case(c)
                result.append(c)
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        vowels = set("AEIOUaeiou")
        for char in ciphertext:
            if char == '_':
                result.append(' ')
            elif char == ' ':
                result.append('_')
            elif char.isalpha():
                c = char
                if c in vowels:
                    c = self._flip_case(c)
                c = self._rot13_char(c)
                result.append(c)
            else:
                result.append(char)
        return ''.join(result)
