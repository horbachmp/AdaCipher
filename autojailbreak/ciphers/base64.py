import base64


class Base64Cipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        plaintext_bytes = plaintext.encode("utf-8")
        ciphertext_bytes = base64.b64encode(plaintext_bytes)
        return ciphertext_bytes.decode("ascii")

    def decrypt(self, ciphertext: str) -> str:
        ciphertext_bytes = ciphertext.encode("ascii")
        plaintext_bytes = base64.b64decode(ciphertext_bytes)
        return plaintext_bytes.decode("utf-8")
