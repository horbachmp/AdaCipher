class Base16AlphabetShift:
    def __init__(self):
        self._enc = {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'a', 'f': 'b'}
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec.get(ch, ch) for ch in ciphertext)
