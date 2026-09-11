class ReverseAlphabetWordCipher:
    def __init__(self):
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                result.append(self.lower[25 - (ord(char) - ord('a'))])
            elif 'A' <= char <= 'Z':
                result.append(self.upper[25 - (ord(char) - ord('A'))])
            else:
                result.append(char)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
