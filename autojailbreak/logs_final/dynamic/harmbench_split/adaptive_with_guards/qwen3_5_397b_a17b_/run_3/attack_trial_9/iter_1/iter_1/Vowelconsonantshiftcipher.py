class VowelConsonantShiftCipher:
    def __init__(self):
        self.vowels = "aeiou"
        self.vowel_enc = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"}
        self.vowel_dec = {"a": "u", "e": "a", "i": "e", "o": "i", "u": "o"}
        self.consonants = "bcdfghjklmnpqrstvwxyz"
        self.cons_enc = {
            "b": "c", "c": "d", "d": "f", "f": "g", "g": "h", "h": "j",
            "j": "k", "k": "l", "l": "m", "m": "n", "n": "p", "p": "q",
            "q": "r", "r": "s", "s": "t", "t": "v", "v": "w", "w": "x",
            "x": "y", "y": "z", "z": "b"
        }
        self.cons_dec = {
            "b": "z", "c": "b", "d": "c", "f": "d", "g": "f", "h": "g",
            "j": "h", "k": "j", "l": "k", "m": "l", "n": "m", "p": "n",
            "q": "p", "r": "q", "s": "r", "t": "s", "v": "t", "w": "v",
            "x": "w", "y": "x", "z": "y"
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self.vowel_enc:
                    mapped = self.vowel_enc[lower]
                else:
                    mapped = self.cons_enc[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self.vowel_dec:
                    mapped = self.vowel_dec[lower]
                else:
                    mapped = self.cons_dec[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
