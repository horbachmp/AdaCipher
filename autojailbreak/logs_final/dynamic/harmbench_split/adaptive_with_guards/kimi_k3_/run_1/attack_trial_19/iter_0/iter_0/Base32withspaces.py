class Base32WithSpaces:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        import base64
        encoded = base64.b32encode(plaintext.encode("ascii")).decode("ascii").rstrip("=")
        return " ".join(encoded)

    def decrypt(self, ciphertext: str) -> str:
        import base64
        s = "".join(ciphertext.split())
        padding = "=" * ((8 - len(s) % 8) % 8)
        return base64.b32decode(s + padding).decode("ascii")
