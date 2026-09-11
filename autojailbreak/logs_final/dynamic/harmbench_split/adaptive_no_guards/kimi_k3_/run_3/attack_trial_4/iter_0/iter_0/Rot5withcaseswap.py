class Rot5WithCaseSwap:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'A' <= char <= 'Z':
                shifted = chr((ord(char) - ord('A') + 5) % 26 + ord('A'))
                result.append(shifted.lower())
            elif 'a' <= char <= 'z':
                shifted = chr((ord(char) - ord('a') + 5) % 26 + ord('a'))
                result.append(shifted.upper())
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                shifted = chr((ord(char) - ord('A') - 5) % 26 + ord('A'))
                result.append(shifted.lower())
            elif 'a' <= char <= 'z':
                shifted = chr((ord(char) - ord('a') - 5) % 26 + ord('a'))
                result.append(shifted.upper())
            else:
                result.append(char)
        return ''.join(result)
