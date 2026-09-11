class Base32AlphabetShift:
    def __init__(self):
        self.shift = 3

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + self.shift) % 26 + ord('A')))
            elif 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + self.shift) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') - self.shift) % 26 + ord('A')))
            elif 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') - self.shift) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)
