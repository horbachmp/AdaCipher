class KeyboardRowReverseCipher:
    def __init__(self):
        lower_map = {
            'q': 'p', 'w': 'o', 'e': 'i', 'r': 'u', 't': 'y',
            'y': 't', 'u': 'r', 'i': 'e', 'o': 'w', 'p': 'q',
            'a': 'l', 's': 'k', 'd': 'j', 'f': 'h', 'g': 'g',
            'h': 'f', 'j': 'd', 'k': 's', 'l': 'a',
            'z': 'm', 'x': 'n', 'c': 'b', 'v': 'v',
            'b': 'c', 'n': 'x', 'm': 'z'
        }
        self._map = lower_map

    def _transform(self, text: str) -> str:
        result = []
        for ch in text:
            lower = ch.lower()
            if lower in self._map:
                mapped = self._map[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
