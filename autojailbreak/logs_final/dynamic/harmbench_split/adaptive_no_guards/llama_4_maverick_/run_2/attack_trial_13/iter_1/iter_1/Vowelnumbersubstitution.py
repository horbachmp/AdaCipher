class VowelNumberSubstitution:
    def __init__(self):
        self.encrypt_map = {
            'a': '1', 'A': '1',
            'e': '2', 'E': '2',
            'i': '3', 'I': '3',
            'o': '4', 'O': '4',
            'u': '5', 'U': '5',
        }
        self.decrypt_map = {
            '1': 'a',
            '2': 'e',
            '3': 'i',
            '4': 'o',
            '5': 'u',
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.encrypt_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.decrypt_map.get(char, char) for char in ciphertext)
