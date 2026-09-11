class AsciiOffsetByThree:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return "".join(chr(ord(c) + 3) for c in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(chr(ord(c) - 3) for c in ciphertext)
