class ConsonantVowelInterchangeCipher:
    def __init__(self):
        lower_map = {
            'a': 'b',
            'b': 'a',
            'e': 'c',
            'c': 'e',
            'i': 'd',
            'd': 'i',
            'o': 'f',
            'f': 'o',
            'u': 'g',
            'g': 'u',
        }
        self._lower_map = lower_map
        self._upper_map = {k.upper(): v.upper() for k, v in lower_map.items()}

    def _transform(self, text: str) -> str:
        result = []
        for ch in text:
            if ch in self._lower_map:
                result.append(self._lower_map[ch])
            elif ch in self._upper_map:
                result.append(self._upper_map[ch])
            else:
                result.append(ch)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
