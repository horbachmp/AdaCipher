class AtbashWithCasePreservation:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if 'a' <= char <= 'z':
                result.append(chr(ord('z') - (ord(char) - ord('a'))))
            elif 'A' <= char <= 'Z':
                result.append(chr(ord('Z') - (ord(char) - ord('A'))))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if 'a' <= char <= 'z':
                result.append(chr(ord('z') - (ord(char) - ord('a'))))
            elif 'A' <= char <= 'Z':
                result.append(chr(ord('Z') - (ord(char) - ord('A'))))
            else:
                result.append(char)
        return ''.join(result)
