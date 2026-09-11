class FixedVowelConsonantInversion:
    def __init__(self):
        self._map = {
            'a': 'u', 'u': 'a',
            'e': 'o', 'o': 'e',
            'i': 'i',
            'b': 'z', 'z': 'b',
            'c': 'y', 'y': 'c',
            'd': 'x', 'x': 'd',
            'f': 'w', 'w': 'f',
            'g': 'v', 'v': 'g',
            'h': 't', 't': 'h',
            'j': 's', 's': 'j',
            'k': 'r', 'r': 'k',
            'l': 'p', 'p': 'l',
            'm': 'n', 'n': 'm',
            'q': 'q'
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            lower = ch.lower()
            if lower in self._map:
                mapped = self._map[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
