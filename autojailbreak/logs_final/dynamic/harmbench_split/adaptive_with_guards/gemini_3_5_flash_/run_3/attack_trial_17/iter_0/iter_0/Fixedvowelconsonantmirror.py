class FixedVowelConsonantMirror:
    def __init__(self):
        self._mapping = {
            'a': 'u', 'e': 'o', 'i': 'i', 'o': 'e', 'u': 'a',
            'b': 'z', 'c': 'y', 'd': 'x', 'f': 'w', 'g': 'v',
            'h': 't', 'j': 's', 'k': 'r', 'l': 'q', 'm': 'p',
            'n': 'n', 'p': 'm', 'q': 'l', 'r': 'k', 's': 'j',
            't': 'h', 'v': 'g', 'w': 'f', 'x': 'd', 'y': 'c',
            'z': 'b'
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            lower = ch.lower()
            if lower in self._mapping:
                mapped = self._mapping[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
