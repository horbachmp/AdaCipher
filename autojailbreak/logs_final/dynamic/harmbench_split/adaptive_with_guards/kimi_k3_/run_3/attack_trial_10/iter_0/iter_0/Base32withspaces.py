class Base32WithSpaces:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        import base64
        encoded = base64.b32encode(plaintext.encode("utf-8")).decode("ascii")
        return " ".join(encoded)

    def decrypt(self, ciphertext: str) -> str:
        import base64
        compact = ciphertext.replace(" ", "")
        return base64.b32decode(compact.encode("ascii")).decode("utf-8")
