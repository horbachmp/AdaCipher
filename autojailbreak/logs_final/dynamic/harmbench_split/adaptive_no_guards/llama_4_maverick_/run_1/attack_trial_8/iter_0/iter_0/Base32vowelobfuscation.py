class Base32VowelObfuscation:
    def __init__(self):
        self.encrypt_map = {
            'a': '2',
            'e': '3',
            'i': '4',
            'o': '5',
            'u': '6',
            'A': '7',
            'E': '8',
            'I': '9',
            'O': '0',
            'U': 'Y',
        }
        self.decrypt_map = {v: k for k, v in self.encrypt_map.items()}

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.encrypt_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.decrypt_map.get(ch, ch) for ch in ciphertext)
