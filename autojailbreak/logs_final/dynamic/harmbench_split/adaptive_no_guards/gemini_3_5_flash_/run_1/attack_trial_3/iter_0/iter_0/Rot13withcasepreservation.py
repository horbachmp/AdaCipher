class Rot13WithCasePreservation:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            elif 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') - 13) % 26 + ord('A')))
            elif 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') - 13) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)
