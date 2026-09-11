class FixedVowelSubstitutionCipher:
    def __init__(self):
        self.enc_map = {
            'a': '@', 'A': '#',
            'e': '3', 'E': '&',
            'i': '1', 'I': '!',
            'o': '0', 'O': '*',
            'u': '_', 'U': '^',
        }
        self.dec_map = {v: k for k, v in self.enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.dec_map.get(ch, ch) for ch in ciphertext)
