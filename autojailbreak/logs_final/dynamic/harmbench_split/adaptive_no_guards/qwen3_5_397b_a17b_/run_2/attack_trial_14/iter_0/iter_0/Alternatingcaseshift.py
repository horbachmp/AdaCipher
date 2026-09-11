class AlternatingCaseShift:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'A' <= char <= 'Z':
                result.append(chr(((ord(char) - 65 + 3) % 26) + 65))
            elif 'a' <= char <= 'z':
                result.append(chr(((ord(char) - 97 - 3) % 26) + 97))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                result.append(chr(((ord(char) - 65 - 3) % 26) + 65))
            elif 'a' <= char <= 'z':
                result.append(chr(((ord(char) - 97 + 3) % 26) + 97))
            else:
                result.append(char)
        return ''.join(result)
