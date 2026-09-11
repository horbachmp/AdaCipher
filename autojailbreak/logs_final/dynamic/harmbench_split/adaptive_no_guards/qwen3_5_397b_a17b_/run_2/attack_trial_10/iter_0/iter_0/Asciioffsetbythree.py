class AsciiOffsetByThree:
    def __init__(self):
        self.shift = 3

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            o = ord(ch)
            if 32 <= o <= 126:
                result.append(chr(((o - 32 + self.shift) % 95) + 32))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            o = ord(ch)
            if 32 <= o <= 126:
                result.append(chr(((o - 32 - self.shift) % 95) + 32))
            else:
                result.append(ch)
        return "".join(result)
