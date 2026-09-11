class VowelConsonantSwapCipher:
    def __init__(self):
        self._vowel_map_upper = {
            "A": "U",
            "E": "O",
            "I": "I",
            "O": "E",
            "U": "A",
        }
        self._consonant_map_upper = {
            "B": "Z",
            "C": "Y",
            "D": "X",
            "F": "W",
            "G": "V",
            "H": "T",
            "J": "S",
            "K": "R",
            "L": "Q",
            "M": "P",
            "N": "N",
            "P": "M",
            "Q": "L",
            "R": "K",
            "S": "J",
            "T": "H",
            "V": "G",
            "W": "F",
            "X": "D",
            "Y": "C",
            "Z": "B",
        }

    def _transform_char(self, char: str) -> str:
        upper = char.upper()
        if upper in self._vowel_map_upper:
            mapped = self._vowel_map_upper[upper]
        elif upper in self._consonant_map_upper:
            mapped = self._consonant_map_upper[upper]
        else:
            return char
        return mapped if char.isupper() else mapped.lower()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._transform_char(char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._transform_char(char) for char in ciphertext)
