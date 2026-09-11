class Rot13WithDigitComplement:
    def __init__(self):
        pass

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            if 'A' <= char <= 'Z':
                result.append(chr(((ord(char) - 65 + 13) % 26) + 65))
            elif 'a' <= char <= 'z':
                result.append(chr(((ord(char) - 97 + 13) % 26) + 97))
            elif '0' <= char <= '9':
                result.append(str(9 - int(char)))
            else:
                result.append(char)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
