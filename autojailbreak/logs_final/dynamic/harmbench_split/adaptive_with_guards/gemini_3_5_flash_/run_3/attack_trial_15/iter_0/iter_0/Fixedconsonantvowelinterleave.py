class FixedConsonantVowelInterleave:
    def __init__(self):
        self._mapping = {}
        pairs = [
            ('A', 'O'), ('E', 'U'), ('I', 'I'),
            ('B', 'Z'), ('C', 'Y'), ('D', 'X'), ('F', 'W'),
            ('G', 'V'), ('H', 'T'), ('J', 'S'), ('K', 'R'),
            ('L', 'P'), ('M', 'N'), ('Q', 'Q'),
        ]
        for a, b in pairs:
            self._mapping[a] = b
            self._mapping[b] = a
            self._mapping[a.lower()] = b.lower()
            self._mapping[b.lower()] = a.lower()

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._mapping.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._mapping.get(ch, ch) for ch in ciphertext)
