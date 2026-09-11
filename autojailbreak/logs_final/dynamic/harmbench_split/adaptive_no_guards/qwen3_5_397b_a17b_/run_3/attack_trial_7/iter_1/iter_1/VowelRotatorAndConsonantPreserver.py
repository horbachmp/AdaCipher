class VowelRotatorAndConsonantPreserver:
    def __init__(self):
        self._enc = {
            'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
            'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
        }
        self._dec = {
            'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o',
            'A': 'U', 'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O'
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec.get(ch, ch) for ch in ciphertext)
