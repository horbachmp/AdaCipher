class VowelConsonantSplitReverseCipher:
    def __init__(self):
        self._mapping = {
            'A': 'U', 'E': 'O', 'I': 'I', 'O': 'E', 'U': 'A',
            'B': 'Z', 'C': 'Y', 'D': 'X', 'F': 'W', 'G': 'V', 'H': 'T',
            'J': 'S', 'K': 'R', 'L': 'Q', 'M': 'P', 'N': 'N', 'P': 'M',
            'Q': 'L', 'R': 'K', 'S': 'J', 'T': 'H', 'V': 'G', 'W': 'F',
            'X': 'D', 'Y': 'C', 'Z': 'B'
        }
        self._mapping.update({k.lower(): v.lower() for k, v in self._mapping.items()})

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._mapping.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._mapping.get(ch, ch) for ch in ciphertext)
