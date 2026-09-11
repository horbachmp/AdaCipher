class Asciishiftbyfive:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return "".join(chr(ord(char) + 5) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(chr(ord(char) - 5) for char in ciphertext)
