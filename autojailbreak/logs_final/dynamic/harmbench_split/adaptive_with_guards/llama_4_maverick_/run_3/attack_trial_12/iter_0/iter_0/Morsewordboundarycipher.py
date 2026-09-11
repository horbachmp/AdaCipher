class MorseWordBoundaryCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        words = plaintext.split(" ")
        return "///".join(word[::-1] for word in words)

    def decrypt(self, ciphertext: str) -> str:
        words = ciphertext.split("///")
        return " ".join(word[::-1] for word in words)
