class Base16HexNoSpaces:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return ''.join(f'{ord(ch):02x}' for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(chr(int(ciphertext[i:i+2], 16)) for i in range(0, len(ciphertext), 2))
