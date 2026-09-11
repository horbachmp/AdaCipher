class VowelToSymbolAndSpaceToPlusCipher:
    def __init__(self):
        self.encrypt_map = {
            "a": "@", "A": "@",
            "e": "#", "E": "#",
            "i": "!", "I": "!",
            "o": "0", "O": "0",
            "u": "*", "U": "*",
            " ": "+",
        }
        self.decrypt_map = {
            "+": " ",
            "@": "a",
            "#": "e",
            "!": "i",
            "0": "o",
            "*": "u",
        }

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.encrypt_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.decrypt_map.get(ch, ch) for ch in ciphertext)
