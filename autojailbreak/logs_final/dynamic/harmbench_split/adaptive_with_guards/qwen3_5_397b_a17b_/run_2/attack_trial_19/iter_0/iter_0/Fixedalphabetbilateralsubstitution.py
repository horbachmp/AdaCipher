class FixedAlphabetBilateralSubstitution:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'a' <= char <= 'z':
                result.append(chr(219 - ord(char)))
            elif 'A' <= char <= 'Z':
                result.append(chr(155 - ord(char)))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'a' <= char <= 'z':
                result.append(chr(219 - ord(char)))
            elif 'A' <= char <= 'Z':
                result.append(chr(155 - ord(char)))
            else:
                result.append(char)
        return ''.join(result)
