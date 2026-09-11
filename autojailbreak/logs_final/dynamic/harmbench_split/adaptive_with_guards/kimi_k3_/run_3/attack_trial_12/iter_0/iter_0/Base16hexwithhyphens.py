class Base16HexWithHyphens:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        return "-".join(f"{ord(ch):02x}" for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        if ciphertext == "":
            return ""
        return "".join(chr(int(part, 16)) for part in ciphertext.split("-"))
