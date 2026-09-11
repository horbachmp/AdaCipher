class FixedKeyboardDiagonalSubstitution:
    def __init__(self):
        pairs = [
            ('Q', 'A'), ('W', 'S'), ('E', 'D'), ('R', 'F'), ('T', 'G'),
            ('Y', 'H'), ('U', 'J'), ('I', 'K'), ('O', 'L'), ('P', 'Z'),
            ('X', 'C'), ('V', 'B'), ('N', 'M')
        ]
        self._map = {}
        for a, b in pairs:
            self._map[a] = b
            self._map[b] = a
            self._map[a.lower()] = b.lower()
            self._map[b.lower()] = a.lower()

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._map.get(ch, ch) for ch in ciphertext)
