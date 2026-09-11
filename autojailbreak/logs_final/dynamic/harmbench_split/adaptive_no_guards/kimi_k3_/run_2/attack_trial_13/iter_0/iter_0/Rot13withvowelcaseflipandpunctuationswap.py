class Rot13WithVowelCaseFlipAndPunctuationSwap:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

    def _rot13_char(self, char: str) -> str:
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        if 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        return char

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                ch = self._rot13_char(char)
                if ch in self.vowels:
                    ch = ch.swapcase()
                result.append(ch)
            elif char == '!':
                result.append('?')
            elif char == '?':
                result.append('!')
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char == '!':
                char = '?'
            elif char == '?':
                char = '!'
            if char.isalpha():
                if char in self.vowels:
                    char = char.swapcase()
                char = self._rot13_char(char)
            result.append(char)
        return ''.join(result)
