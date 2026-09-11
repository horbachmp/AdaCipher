class Rot13WithCasePreservation:
    def __init__(self):
        pass

    def _rot13_char(self, char: str) -> str:
        if 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        return char

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._rot13_char(char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._rot13_char(char) for char in ciphertext)
