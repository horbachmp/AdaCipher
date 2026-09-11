class AlternatingCaseRot13:
    def __init__(self):
        pass

    def _rot13(self, char: str) -> str:
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        if 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        return char

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                rotated = self._rot13(char)
                result.append(rotated.swapcase())
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char.isalpha():
                swapped = char.swapcase()
                result.append(self._rot13(swapped))
            else:
                result.append(char)
        return ''.join(result)
