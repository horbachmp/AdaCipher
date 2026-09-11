class VowelSubstitutionWithFixedSymbols:
    def __init__(self):
        self.encrypt_map = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': '_'}
        self.decrypt_map = {'@': 'a', '3': 'e', '1': 'i', '0': 'o', '_': 'u'}

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.encrypt_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.decrypt_map.get(ch, ch) for ch in ciphertext)
