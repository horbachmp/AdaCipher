class Base36AlternateSubstitution:
    def __init__(self):
        self._enc = {
            'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's',
            'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k',
            'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
            'y': 'b', 'z': 'a'
        }
        self._dec = self._enc

    def encrypt(self, plaintext: str) -> str:
        plaintext = plaintext.lower()
        return ''.join(self._enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec.get(ch, ch) for ch in ciphertext)
