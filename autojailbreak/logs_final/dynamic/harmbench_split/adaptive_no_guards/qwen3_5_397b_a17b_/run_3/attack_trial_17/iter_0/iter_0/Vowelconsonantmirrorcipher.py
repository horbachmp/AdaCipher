class VowelConsonantMirrorCipher:
    def __init__(self):
        self._mapping = {
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
            'l': 'q', 'q': 'l',
            'm': 'p', 'p': 'm',
            'n': 'n',
        }

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            lower = char.lower()
            if lower in self._mapping:
                mapped = self._mapping[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
