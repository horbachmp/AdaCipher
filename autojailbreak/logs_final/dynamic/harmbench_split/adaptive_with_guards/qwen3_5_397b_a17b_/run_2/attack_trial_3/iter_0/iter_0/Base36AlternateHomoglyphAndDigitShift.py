class Base36AlternateHomoglyphAndDigitShift:
    def __init__(self):
        self._enc = {
            'a': '4', 'b': '8', 'c': '[', 'd': ']', 'e': '3', 'f': '%', 'g': '9', 'h': '#',
            'i': '1', 'j': 'j', 'k': 'k', 'l': 'L', 'm': 'm', 'n': '^', 'o': '0', 'p': 'p',
            'q': 'q', 'r': '2', 's': '5', 't': '7', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x',
            'y': 'y', 'z': 'z'
        }
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._enc.get(ch.lower(), ch) if ch.isalpha() else ch for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec.get(ch, ch) for ch in ciphertext)
