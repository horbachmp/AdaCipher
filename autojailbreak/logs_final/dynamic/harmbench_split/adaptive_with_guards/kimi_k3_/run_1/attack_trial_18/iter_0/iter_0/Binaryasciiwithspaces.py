class BinaryAsciiWithSpaces:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return " ".join(format(ord(ch), "08b") for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        if ciphertext == "":
            return ""
        return "".join(chr(int(bits, 2)) for bits in ciphertext.split(" "))
