class Rot18WithSpacePreservation:
    def __init__(self):
        pass

    def _transform(self, text: str) -> str:
        result = []
        for c in text:
            if 'A' <= c <= 'Z':
                result.append(chr(((ord(c) - 65 + 13) % 26) + 65))
            elif 'a' <= c <= 'z':
                result.append(chr(((ord(c) - 97 + 13) % 26) + 97))
            elif '0' <= c <= '9':
                result.append(chr(((ord(c) - 48 + 5) % 10) + 48))
            else:
                result.append(c)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
