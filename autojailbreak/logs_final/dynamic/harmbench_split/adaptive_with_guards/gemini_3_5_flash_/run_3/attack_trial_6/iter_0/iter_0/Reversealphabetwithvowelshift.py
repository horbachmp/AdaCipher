class ReverseAlphabetWithVowelShift:
    def __init__(self):
        self._vowels_upper = "AEIOU"
        self._vowels_lower = "aeiou"
        self._consonants_upper = "BCDFGHJKLMNPQRSTVWXYZ"
        self._consonants_lower = "bcdfghjklmnpqrstvwxyz"
        self._vowel_enc = {
            "A": "E", "E": "I", "I": "O", "O": "U", "U": "A",
            "a": "e", "e": "i", "i": "o", "o": "u", "u": "a",
        }
        self._vowel_dec = {
            "A": "U", "E": "A", "I": "E", "O": "I", "U": "O",
            "a": "u", "e": "a", "i": "e", "o": "i", "u": "o",
        }
        self._cons_map = {
            "B": "Z", "C": "Y", "D": "X", "F": "W", "G": "V", "H": "T", "J": "S",
            "K": "R", "L": "Q", "M": "P", "N": "N", "P": "M", "Q": "L", "R": "K",
            "S": "J", "T": "H", "V": "G", "W": "F", "X": "D", "Y": "C", "Z": "B",
            "b": "z", "c": "y", "d": "x", "f": "w", "g": "v", "h": "t", "j": "s",
            "k": "r", "l": "q", "m": "p", "n": "n", "p": "m", "q": "l", "r": "k",
            "s": "j", "t": "h", "v": "g", "w": "f", "x": "d", "y": "c", "z": "b",
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._vowel_enc:
                result.append(self._vowel_enc[ch])
            elif ch.isalpha():
                result.append(self._cons_map.get(ch, ch))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._vowel_dec:
                result.append(self._vowel_dec[ch])
            elif ch.isalpha():
                result.append(self._cons_map.get(ch, ch))
            else:
                result.append(ch)
        return "".join(result)
