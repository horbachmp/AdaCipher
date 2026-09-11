class ReverseTextCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return plaintext[::-1]

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext[::-1]
