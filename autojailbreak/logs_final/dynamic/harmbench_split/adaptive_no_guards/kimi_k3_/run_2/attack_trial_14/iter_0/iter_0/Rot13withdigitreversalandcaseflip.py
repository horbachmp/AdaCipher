class Rot13WithDigitReversalAndCaseFlip:
    def __init__(self):
        pass

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            if char.isalpha():
                if 'a' <= char <= 'z':
                    shifted = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
                else:
                    shifted = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
                result.append(shifted.swapcase())
            elif char.isdigit():
                result.append(str(9 - int(char)))
            else:
                result.append(char)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
