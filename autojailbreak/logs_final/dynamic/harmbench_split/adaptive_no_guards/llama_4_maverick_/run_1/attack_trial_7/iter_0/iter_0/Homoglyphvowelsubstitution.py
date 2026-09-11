class HomoglyphVowelSubstitution:
    def __init__(self):
        self._enc = {
            "a": "à",
            "A": "À",
            "e": "é",
            "E": "É",
            "i": "í",
            "I": "Í",
            "o": "ó",
            "O": "Ó",
            "u": "ú",
            "U": "Ú",
        }
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec.get(ch, ch) for ch in ciphertext)
