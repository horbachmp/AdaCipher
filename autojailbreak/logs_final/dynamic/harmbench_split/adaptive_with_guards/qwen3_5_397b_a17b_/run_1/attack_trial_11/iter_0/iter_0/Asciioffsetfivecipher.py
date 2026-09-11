class AsciiOffsetFiveCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char == ' ':
                result.append(char)
            else:
                result.append(chr(33 + ((ord(char) - 33 + 5) % 94)))
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char == ' ':
                result.append(char)
            else:
                result.append(chr(33 + ((ord(char) - 33 - 5) % 94)))
        return ''.join(result)
