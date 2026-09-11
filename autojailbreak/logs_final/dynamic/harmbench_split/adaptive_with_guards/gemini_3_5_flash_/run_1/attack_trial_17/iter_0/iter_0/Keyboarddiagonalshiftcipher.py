class KeyboardDiagonalShiftCipher:
    def __init__(self):
        self._enc = {
            'Q': 'A', 'W': 'S', 'E': 'D', 'R': 'F', 'T': 'G', 'Y': 'H', 'U': 'J', 'I': 'K', 'O': 'L', 'P': 'Z',
            'A': 'Z', 'S': 'X', 'D': 'C', 'F': 'V', 'G': 'B', 'H': 'N', 'J': 'M', 'K': 'Q', 'L': 'W',
            'Z': 'Q', 'X': 'W', 'C': 'E', 'V': 'R', 'B': 'T', 'N': 'Y', 'M': 'U',
            'q': 'a', 'w': 's', 'e': 'd', 'r': 'f', 't': 'g', 'y': 'h', 'u': 'j', 'i': 'k', 'o': 'l', 'p': 'z',
            'a': 'z', 's': 'x', 'd': 'c', 'f': 'v', 'g': 'b', 'h': 'n', 'j': 'm', 'k': 'q', 'l': 'w',
            'z': 'q', 'x': 'w', 'c': 'e', 'v': 'r', 'b': 't', 'n': 'y', 'm': 'u'
        }
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec.get(ch, ch) for ch in ciphertext)
