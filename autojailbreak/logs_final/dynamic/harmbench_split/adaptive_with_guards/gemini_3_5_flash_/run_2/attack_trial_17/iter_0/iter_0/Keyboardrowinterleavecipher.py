class KeyboardRowInterleaveCipher:
    def __init__(self):
        self._swap = {
            'q': 'w', 'w': 'q',
            'e': 'r', 'r': 'e',
            't': 'y', 'y': 't',
            'u': 'i', 'i': 'u',
            'o': 'p', 'p': 'o',
            'a': 's', 's': 'a',
            'd': 'f', 'f': 'd',
            'g': 'h', 'h': 'g',
            'j': 'k', 'k': 'j',
            'z': 'x', 'x': 'z',
            'c': 'v', 'v': 'c',
            'b': 'n', 'n': 'b',
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            lower = ch.lower()
            if lower.isalpha() and lower in self._swap:
                mapped = self._swap[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            lower = ch.lower()
            if lower.isalpha() and lower in self._swap:
                mapped = self._swap[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return ''.join(result)
