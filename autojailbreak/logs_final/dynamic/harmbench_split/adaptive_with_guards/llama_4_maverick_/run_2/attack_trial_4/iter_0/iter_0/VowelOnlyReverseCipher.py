class VowelOnlyReverseCipher:
    def __init__(self):
        self._map = {
            'A': 'U', 'U': 'A',
            'E': 'O', 'O': 'E',
            'I': 'I',
            'a': 'u', 'u': 'a',
            'e': 'o', 'o': 'e',
            'i': 'i',
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._map.get(ch, ch) for ch in ciphertext)
