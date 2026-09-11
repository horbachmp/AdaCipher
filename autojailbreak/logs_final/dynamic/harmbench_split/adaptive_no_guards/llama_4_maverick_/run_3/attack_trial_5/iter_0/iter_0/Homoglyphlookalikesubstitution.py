class HomoglyphLookalikeSubstitution:
    def __init__(self):
        self._enc_map = {
            "a": "\u0430",
            "c": "\u0441",
            "e": "\u0435",
            "o": "\u043e",
            "p": "\u0440",
            "x": "\u0445",
            "y": "\u0443",
        }
        self._dec_map = {v: k for k, v in self._enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec_map.get(ch, ch) for ch in ciphertext)
