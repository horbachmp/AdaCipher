class ReverseWordCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)

    def _transform(self, text: str) -> str:
        result = []
        current = []
        for char in text:
            if char.isalpha():
                current.append(char)
            else:
                if current:
                    result.append(''.join(reversed(current)))
                    current = []
                result.append(char)
        if current:
            result.append(''.join(reversed(current)))
        return ''.join(result)
