class ReverseAlphabetWithVowelPreservation:
    def __init__(self):
        self._vowels = set("AEIOUaeiou")
        self._lower_map = {
            "b": "y", "c": "x", "d": "w", "f": "v", "g": "t", "h": "s", "j": "q",
            "k": "p", "l": "o", "m": "n", "n": "m", "p": "k", "q": "j", "r": "i",
            "s": "h", "t": "g", "v": "f", "w": "d", "x": "c", "y": "b", "z": "a"
        }
        self._upper_map = {k.upper(): v.upper() for k, v in self._lower_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if not ch.isalpha() or ch in self._vowels:
                result.append(ch)
            elif ch.islower():
                result.append(self._lower_map.get(ch, ch))
            else:
                result.append(self._upper_map.get(ch, ch))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if not ch.isalpha() or ch in self._vowels:
                result.append(ch)
            elif ch.islower():
                result.append(self._lower_map.get(ch, ch))
            else:
                result.append(self._upper_map.get(ch, ch))
        return "".join(result)
