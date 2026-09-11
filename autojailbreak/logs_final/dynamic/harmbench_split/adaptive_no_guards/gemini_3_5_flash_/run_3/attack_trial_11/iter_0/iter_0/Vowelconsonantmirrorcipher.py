class VowelConsonantMirrorCipher:
    def __init__(self):
        self.enc_map = {
            'a': 'u', 'e': 'o', 'i': 'i', 'o': 'e', 'u': 'a',
            'b': 'z', 'c': 'y', 'd': 'x', 'f': 'w', 'g': 'v', 'h': 't',
            'j': 's', 'k': 'r', 'l': 'q', 'm': 'p', 'n': 'n', 'p': 'm',
            'q': 'l', 'r': 'k', 's': 'j', 't': 'h', 'v': 'g', 'w': 'f',
            'x': 'd', 'y': 'c', 'z': 'b'
        }
        self.enc_map.update({k.upper(): v.upper() for k, v in self.enc_map.items()})

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.enc_map.get(ch, ch) for ch in ciphertext)
