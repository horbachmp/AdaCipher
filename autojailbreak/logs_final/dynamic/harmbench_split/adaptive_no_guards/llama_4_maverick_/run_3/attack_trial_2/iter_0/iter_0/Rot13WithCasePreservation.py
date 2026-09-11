class ROT13WithCasePreservation:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'a' <= char <= 'z':
                result.append(chr(((ord(char) - 97 + 13) % 26) + 97))
            elif 'A' <= char <= 'Z':
                result.append(chr(((ord(char) - 65 + 13) % 26) + 65))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'a' <= char <= 'z':
                result.append(chr(((ord(char) - 97 + 13) % 26) + 97))
            elif 'A' <= char <= 'Z':
                result.append(chr(((ord(char) - 65 + 13) % 26) + 65))
            else:
                result.append(char)
        return ''.join(result)
