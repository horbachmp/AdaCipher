class VowelRot13Cipher:
    def __init__(self):
        self._enc_map = {
            "a": "n",
            "e": "r",
            "i": "v",
            "o": "b",
            "u": "h",
            "A": "N",
            "E": "R",
            "I": "V",
            "O": "B",
            "U": "H",
        }
        self._dec_map = {v: k for k, v in self._enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec_map.get(ch, ch) for ch in ciphertext)
