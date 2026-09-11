class ReverseWordOrderWithRot5:
    def __init__(self):
        pass

    def _rot5(self, text: str, shift: int) -> str:
        result = []
        for char in text:
            if 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            elif 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        words = plaintext.split(' ')
        reversed_words = words[::-1]
        shifted_words = [self._rot5(word, 5) for word in reversed_words]
        return ' '.join(shifted_words)

    def decrypt(self, ciphertext: str) -> str:
        unshifted = self._rot5(ciphertext, -5)
        words = unshifted.split(' ')
        return ' '.join(words[::-1])
