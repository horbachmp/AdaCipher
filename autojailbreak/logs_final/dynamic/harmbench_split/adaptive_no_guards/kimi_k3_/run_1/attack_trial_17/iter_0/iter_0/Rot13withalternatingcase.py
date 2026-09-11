class Rot13WithAlternatingCase:
    def __init__(self):
        pass

    def _rot13_char(self, char: str) -> str:
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        if 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        return char

    def _transform(self, text: str) -> str:
        result = []
        alpha_counter = 0
        for char in text:
            if char.isalpha():
                shifted = self._rot13_char(char)
                if alpha_counter % 2 == 0:
                    result.append(shifted.upper())
                else:
                    result.append(shifted.lower())
                alpha_counter += 1
            else:
                result.append(char)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
