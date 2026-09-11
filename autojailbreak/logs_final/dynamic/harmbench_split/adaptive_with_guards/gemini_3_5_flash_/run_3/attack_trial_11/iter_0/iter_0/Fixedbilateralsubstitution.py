class FixedBilateralSubstitution:
    def __init__(self):
        pairs = {
            'A': 'P', 'B': 'Q', 'C': 'R', 'D': 'S', 'E': 'T', 'F': 'U', 'G': 'V',
            'H': 'W', 'I': 'X', 'J': 'Y', 'K': 'Z', 'L': 'M', 'N': 'O'
        }
        self._mapping = {}
        for a, b in pairs.items():
            self._mapping[a] = b
            self._mapping[b] = a
            self._mapping[a.lower()] = b.lower()
            self._mapping[b.lower()] = a.lower()

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._mapping.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._mapping.get(char, char) for char in ciphertext)
