class ReverseWordOrderWithCharacterReversal:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        parts = plaintext.split(" ")
        return " ".join(part[::-1] for part in parts)

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split(" ")
        return " ".join(part[::-1] for part in parts)
