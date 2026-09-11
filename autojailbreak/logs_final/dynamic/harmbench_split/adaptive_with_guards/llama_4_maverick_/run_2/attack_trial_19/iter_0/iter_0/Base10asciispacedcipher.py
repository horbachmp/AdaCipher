class Base10AsciiSpacedCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return " ".join(str(ord(char)) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        if ciphertext == "":
            return ""
        return "".join(chr(int(part)) for part in ciphertext.split(" "))
