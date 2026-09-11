class VowelConsonantAlternatingCaseCipher:
    def __init__(self):
        self._vowels = "aeiou"
        self._vowel_next = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"}
        self._vowel_prev = {"a": "u", "e": "a", "i": "e", "o": "i", "u": "o"}
        self._consonants = "bcdfghjklmnpqrstvwxyz"
        self._consonant_next = {
            "b": "c", "c": "d", "d": "f", "f": "g", "g": "h", "h": "j", "j": "k",
            "k": "l", "l": "m", "m": "n", "n": "p", "p": "q", "q": "r", "r": "s",
            "s": "t", "t": "v", "v": "w", "w": "x", "x": "y", "y": "z", "z": "b"
        }
        self._consonant_prev = {
            "b": "z", "c": "b", "d": "c", "f": "d", "g": "f", "h": "g", "j": "h",
            "k": "j", "l": "k", "m": "l", "n": "m", "p": "n", "q": "p", "r": "q",
            "s": "r", "t": "s", "v": "t", "w": "v", "x": "w", "y": "x", "z": "y"
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            low = ch.lower()
            if low in self._vowel_next:
                mapped = self._vowel_next[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            elif low in self._consonant_next:
                mapped = self._consonant_next[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            low = ch.lower()
            if low in self._vowel_prev:
                mapped = self._vowel_prev[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            elif low in self._consonant_prev:
                mapped = self._consonant_prev[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
