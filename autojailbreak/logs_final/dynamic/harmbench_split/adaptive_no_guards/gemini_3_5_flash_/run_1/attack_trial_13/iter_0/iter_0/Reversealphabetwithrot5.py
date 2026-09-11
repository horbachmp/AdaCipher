class ReverseAlphabetWithRot5:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'A' <= char <= 'Z':
                result.append(chr(155 - ord(char)))
            elif 'a' <= char <= 'z':
                result.append(chr(219 - ord(char)))
            elif '0' <= char <= '9':
                result.append(str((int(char) + 5) % 10))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                result.append(chr(155 - ord(char)))
            elif 'a' <= char <= 'z':
                result.append(chr(219 - ord(char)))
            elif '0' <= char <= '9':
                result.append(str((int(char) + 5) % 10))
            else:
                result.append(char)
        return ''.join(result)
