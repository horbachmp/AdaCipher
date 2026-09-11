class HomoglyphLeetSpeakV4:
    def __init__(self):
        self._enc_map = {
            "a": "4",
            "A": "4",
            "e": "3",
            "E": "3",
            "i": "1",
            "I": "1",
            "o": "0",
            "O": "0",
            "s": "5",
            "S": "5",
            "t": "7",
            "T": "7",
            "b": "8",
            "B": "8",
            "g": "9",
            "G": "9",
            "l": "|",
            "L": "|",
        }
        self._dec_map = {
            "4": "a",
            "3": "e",
            "1": "i",
            "0": "o",
            "5": "s",
            "7": "t",
            "8": "b",
            "9": "g",
            "|": "l",
        }

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._enc_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._dec_map.get(char, char) for char in ciphertext)
