class VowelToNumberAndSpaceToUnderscoreCipher:
    def __init__(self):
        self._enc_map = {
            "a": "1", "e": "2", "i": "3", "o": "4", "u": "5",
            "A": "1", "E": "2", "I": "3", "O": "4", "U": "5",
            " ": "_",
        }
        self._dec_map = {
            "1": "a", "2": "e", "3": "i", "4": "o", "5": "u",
            "_": " ",
        }

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec_map.get(ch, ch) for ch in ciphertext)
