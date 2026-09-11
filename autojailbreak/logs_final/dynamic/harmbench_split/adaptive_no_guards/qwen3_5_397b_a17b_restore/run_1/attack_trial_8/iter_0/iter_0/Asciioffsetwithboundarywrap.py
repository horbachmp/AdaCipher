class AsciiOffsetWithBoundaryWrap:
    def __init__(self, offset: int = 4):
        self.offset = offset

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char == ' ' or char == '\n':
                result.append(char)
            else:
                v = ord(char)
                e = 33 + ((v - 33 + self.offset) % 94)
                result.append(chr(e))
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char == ' ' or char == '\n':
                result.append(char)
            else:
                e = ord(char)
                v = 33 + ((e - 33 - self.offset) % 94)
                result.append(chr(v))
        return ''.join(result)
