class Rot13WithDigitShift:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'A' <= char <= 'Z':
                result.append(chr((ord(char) - 65 + 13) % 26 + 65))
            elif 'a' <= char <= 'z':
                result.append(chr((ord(char) - 97 + 13) % 26 + 97))
            elif '0' <= char <= '9':
                result.append(chr((ord(char) - 48 + 5) % 10 + 48))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                result.append(chr((ord(char) - 65 - 13 + 26) % 26 + 65))
            elif 'a' <= char <= 'z':
                result.append(chr((ord(char) - 97 - 13 + 26) % 26 + 97))
            elif '0' <= char <= '9':
                result.append(chr((ord(char) - 48 - 5 + 10) % 10 + 48))
            else:
                result.append(char)
        return ''.join(result)
