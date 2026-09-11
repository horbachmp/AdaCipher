class WordWiseCharacterReversal:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return " ".join(word[::-1] for word in plaintext.split(" "))

    def decrypt(self, ciphertext: str) -> str:
        return " ".join(word[::-1] for word in ciphertext.split(" "))
