class WordWiseCharacterShift:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext, 1)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext, -1)

    def _transform(self, text: str, direction: int) -> str:
        result = []
        for token in text.split():
            i = 1
            transformed = []
            for ch in token:
                if ch.isalpha():
                    base = ord('a') if ch.islower() else ord('A')
                    shift = direction * i
                    transformed.append(chr((ord(ch) - base + shift) % 26 + base))
                    i += 1
                else:
                    transformed.append(ch)
            result.append(''.join(transformed))
        return ' '.join(result)
