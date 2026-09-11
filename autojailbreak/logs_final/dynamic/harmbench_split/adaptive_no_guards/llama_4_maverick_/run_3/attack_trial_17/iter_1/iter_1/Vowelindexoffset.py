class VowelIndexOffset:
    def __init__(self):
        self._enc = str.maketrans({"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"})
        self._dec = str.maketrans({"e": "a", "i": "e", "o": "i", "u": "o", "a": "u"})

    def encrypt(self, plaintext: str) -> str:
        return plaintext.translate(self._enc)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext.translate(self._dec)
