class NoCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return plaintext
    
    def decrypt(self, ciphertext: str) -> str:
        return ciphertext