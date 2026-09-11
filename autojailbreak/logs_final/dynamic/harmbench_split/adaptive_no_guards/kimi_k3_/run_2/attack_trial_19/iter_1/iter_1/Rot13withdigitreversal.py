class Rot13WithDigitReversal:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for c in plaintext:
            if 'A' <= c <= 'Z':
                result.append(chr(((ord(c) - 65 + 13) % 26) + 65))
            elif 'a' <= c <= 'z':
                result.append(chr(((ord(c) - 97 + 13) % 26) + 97))
            elif '0' <= c <= '9':
                result.append(str(9 - int(c)))
            else:
                result.append(c)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for c in ciphertext:
            if 'A' <= c <= 'Z':
                result.append(chr(((ord(c) - 65 - 13) % 26) + 65))
            elif 'a' <= c <= 'z':
                result.append(chr(((ord(c) - 97 - 13) % 26) + 97))
            elif '0' <= c <= '9':
                result.append(str(9 - int(c)))
            else:
                result.append(c)
        return ''.join(result)
