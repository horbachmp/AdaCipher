class FixedConsonantVowelShiftTwo:
    def __init__(self):
        self._vowels_upper = "AEIOU"
        self._vowels_lower = "aeiou"
        self._cons_upper = "BCDFGHJKLMNPQRSTVWXYZ"
        self._cons_lower = "bcdfghjklmnpqrstvwxyz"
        self._enc_vowel = str.maketrans({
            "A": "I", "E": "O", "I": "U", "O": "A", "U": "E",
            "a": "i", "e": "o", "i": "u", "o": "a", "u": "e",
        })
        self._dec_vowel = str.maketrans({
            "A": "O", "E": "U", "I": "A", "O": "E", "U": "I",
            "a": "o", "e": "u", "i": "a", "o": "e", "u": "i",
        })
        enc_cons_src = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
        enc_cons_dst = "YZBCDFGHJKMNPQRSTVWXYyzbcdfghjkmnpqrstvwxy"
        dec_cons_src = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
        dec_cons_dst = "DEFGHJKLMNPQRSTVWXYZABCdefghjklmnpqrstvwxyza"
        self._enc_cons = str.maketrans({
            "B": "Y", "C": "Z", "D": "B", "F": "C", "G": "D", "H": "F", "J": "G", "K": "H",
            "L": "J", "M": "K", "N": "L", "P": "M", "Q": "N", "R": "P", "S": "Q", "T": "R",
            "V": "S", "W": "T", "X": "V", "Y": "W", "Z": "X",
            "b": "y", "c": "z", "d": "b", "f": "c", "g": "d", "h": "f", "j": "g", "k": "h",
            "l": "j", "m": "k", "n": "l", "p": "m", "q": "n", "r": "p", "s": "q", "t": "r",
            "v": "s", "w": "t", "x": "v", "y": "w", "z": "x",
        })
        self._dec_cons = str.maketrans({
            "B": "D", "C": "F", "D": "G", "F": "H", "G": "J", "H": "K", "J": "L", "K": "M",
            "L": "N", "M": "P", "N": "Q", "P": "R", "Q": "S", "R": "T", "S": "V", "T": "W",
            "V": "X", "W": "Y", "X": "Z", "Y": "B", "Z": "C",
            "b": "d", "c": "f", "d": "g", "f": "h", "g": "j", "h": "k", "j": "l", "k": "m",
            "l": "n", "m": "p", "n": "q", "p": "r", "q": "s", "r": "t", "s": "v", "t": "w",
            "v": "x", "w": "y", "x": "z", "y": "b", "z": "c",
        })

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._vowels_upper or ch in self._vowels_lower:
                result.append(ch.translate(self._enc_vowel))
            elif ch.isalpha():
                result.append(ch.translate(self._enc_cons))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._vowels_upper or ch in self._vowels_lower:
                result.append(ch.translate(self._dec_vowel))
            elif ch.isalpha():
                result.append(ch.translate(self._dec_cons))
            else:
                result.append(ch)
        return "".join(result)
