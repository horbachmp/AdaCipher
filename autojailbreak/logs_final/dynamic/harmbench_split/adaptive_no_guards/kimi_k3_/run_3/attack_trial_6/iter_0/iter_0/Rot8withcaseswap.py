class Rot8WithCaseSwap:
    def __init__(self):
        self.shift = 8

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'A' <= char <= 'Z':
                shifted = chr((ord(char) - ord('A') + self.shift) % 26 + ord('A')).lower()
                result.append(shifted)
            elif 'a' <= char <= 'z':
                shifted = chr((ord(char) - ord('a') + self.shift) % 26 + ord('a')).upper()
                result.append(shifted)
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                shifted = chr((ord(char) - ord('A') - self.shift) % 26 + ord('A')).lower()
                result.append(shifted)
            elif 'a' <= char <= 'z':
                shifted = chr((ord(char) - ord('a') - self.shift) % 26 + ord('a')).upper()
                result.append(shifted)
            else:
                result.append(char)
        return ''.join(result)
