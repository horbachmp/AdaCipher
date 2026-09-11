class Rot13WithSpaceToPlus:
    def __init__(self):
        pass

    def _rot13_char(self, char: str) -> str:
        if 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        return char

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char == ' ':
                result.append('+')
            elif char == '+':
                result.append(' ')
            else:
                result.append(self._rot13_char(char))
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char == '+':
                result.append(' ')
            elif char == ' ':
                result.append('+')
            else:
                result.append(self._rot13_char(char))
        return ''.join(result)
