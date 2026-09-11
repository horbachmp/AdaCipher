class Rot13WithCasePreservation:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for c in plaintext:
            if 'a' <= c <= 'z':
                result.append(chr(((ord(c) - 97 + 13) % 26) + 97))
            elif 'A' <= c <= 'Z':
                result.append(chr(((ord(c) - 65 + 13) % 26) + 65))
            else:
                result.append(c)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for c in ciphertext:
            if 'a' <= c <= 'z':
                result.append(chr(((ord(c) - 97 + 13) % 26) + 97))
            elif 'A' <= c <= 'Z':
                result.append(chr(((ord(c) - 65 + 13) % 26) + 65))
            else:
                result.append(c)
        return ''.join(result)
