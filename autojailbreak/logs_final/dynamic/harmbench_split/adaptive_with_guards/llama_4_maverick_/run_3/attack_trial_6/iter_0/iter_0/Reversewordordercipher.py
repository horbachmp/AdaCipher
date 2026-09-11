class ReverseWordOrderCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        tokens = plaintext.split()
        tokens.reverse()
        return " ".join(tokens)

    def decrypt(self, ciphertext: str) -> str:
        tokens = ciphertext.split()
        tokens.reverse()
        return " ".join(tokens)
