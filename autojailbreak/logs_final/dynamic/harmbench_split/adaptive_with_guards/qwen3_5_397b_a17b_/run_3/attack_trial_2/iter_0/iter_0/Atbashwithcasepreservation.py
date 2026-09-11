class AtbashWithCasePreservation:
    def __init__(self):
        pass

    def _transform(self, text: str) -> str:
        result = []
        for ch in text:
            if 'A' <= ch <= 'Z':
                result.append(chr(ord('Z') - (ord(ch) - ord('A'))))
            elif 'a' <= ch <= 'z':
                result.append(chr(ord('z') - (ord(ch) - ord('a'))))
            else:
                result.append(ch)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
