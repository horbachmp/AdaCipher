class Rot18Symmetric:
    def __init__(self):
        pass

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            code = ord(char)
            if 65 <= code <= 90:
                result.append(chr(((code - 65 + 13) % 26) + 65))
            elif 97 <= code <= 122:
                result.append(chr(((code - 97 + 13) % 26) + 97))
            elif 48 <= code <= 57:
                result.append(chr(((code - 48 + 5) % 10) + 48))
            else:
                result.append(char)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
