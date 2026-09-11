class Base16HexEncodingWithPrefix:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return "".join(f".{ord(ch):02x}" for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split(".")
        chars = []
        for part in parts:
            if part == "":
                continue
            chars.append(chr(int(part, 16)))
        return "".join(chars)
