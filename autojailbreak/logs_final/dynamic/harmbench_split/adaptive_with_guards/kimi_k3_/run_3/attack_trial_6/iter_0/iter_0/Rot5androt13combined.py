class Rot5AndRot13Combined:
    def __init__(self):
        pass

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            if 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            elif 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif '0' <= char <= '9':
                result.append(chr((ord(char) - ord('0') + 5) % 10 + ord('0')))
            else:
                result.append(char)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
