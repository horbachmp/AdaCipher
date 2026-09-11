class SimpleAlphabetShiftTwo:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 2) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 2) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') - 2) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') - 2) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)
