class AtbashCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            if 'A' <= char <= 'Z':
                result.append(chr(ord('Z') - (ord(char) - ord('A'))))
            elif 'a' <= char <= 'z':
                result.append(chr(ord('z') - (ord(char) - ord('a'))))
            else:
                result.append(char)
        return ''.join(result)
