class VowelConsonantInterchange:
    def __init__(self):
        self._vowels_lower_enc = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"}
        self._vowels_lower_dec = {"e": "a", "i": "e", "o": "i", "u": "o", "a": "u"}
        self._consonants_lower_enc = {
            "b": "c", "c": "d", "d": "f", "f": "g", "g": "h", "h": "j", "j": "k",
            "k": "l", "l": "m", "m": "n", "n": "p", "p": "q", "q": "r", "r": "s",
            "s": "t", "t": "v", "v": "w", "w": "x", "x": "y", "y": "z", "z": "b"
        }
        self._consonants_lower_dec = {
            "c": "b", "d": "c", "f": "d", "g": "f", "h": "g", "j": "h", "k": "j",
            "l": "k", "m": "l", "n": "m", "p": "n", "q": "p", "r": "q", "s": "r",
            "t": "s", "v": "t", "w": "v", "x": "w", "y": "x", "z": "y", "b": "z"
        }

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            low = ch.lower()
            if low in self._vowels_lower_enc:
                mapped = self._vowels_lower_enc[low]
                out.append(mapped.upper() if ch.isupper() else mapped)
            elif ch.isalpha():
                mapped = self._consonants_lower_enc[low]
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            low = ch.lower()
            if low in self._vowels_lower_dec:
                mapped = self._vowels_lower_dec[low]
                out.append(mapped.upper() if ch.isupper() else mapped)
            elif ch.isalpha():
                mapped = self._consonants_lower_dec[low]
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return "".join(out)
