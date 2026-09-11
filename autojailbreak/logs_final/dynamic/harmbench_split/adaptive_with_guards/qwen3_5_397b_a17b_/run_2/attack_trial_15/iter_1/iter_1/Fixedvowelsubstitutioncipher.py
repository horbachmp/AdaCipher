class FixedVowelSubstitutionCipher:
    def __init__(self):
        self._enc = str.maketrans({
            "a": "1",
            "e": "2",
            "i": "3",
            "o": "4",
            "u": "5",
            "A": "1",
            "E": "2",
            "I": "3",
            "O": "4",
            "U": "5",
        })
        self._dec = str.maketrans({
            "1": "a",
            "2": "e",
            "3": "i",
            "4": "o",
            "5": "u",
        })

    def encrypt(self, plaintext: str) -> str:
        return plaintext.translate(self._enc)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext.translate(self._dec)
