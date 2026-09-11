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
        for ch in text:
            if ch.isalnum():
                current.append(ch)
            else:
                if current:
                    result.extend(reversed(current))
                    current = []
                result.append(ch)
        if current:
            result.extend(reversed(current))
        return "".join(result)
