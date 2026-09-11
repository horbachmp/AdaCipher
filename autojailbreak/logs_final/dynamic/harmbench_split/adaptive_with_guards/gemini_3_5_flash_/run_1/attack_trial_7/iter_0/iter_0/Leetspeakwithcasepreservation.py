class LeetspeakWithCasePreservation:
    def __init__(self):
        self.encrypt_map = {
            'A': '4', 'a': '4',
            'E': '3', 'e': '3',
            'I': '1', 'i': '1',
            'O': '0', 'o': '0',
            'S': '5', 's': '5',
            'T': '7', 't': '7',
        }
        self.decrypt_map = {
            '4': 'a',
            '3': 'e',
            '1': 'i',
            '0': 'o',
            '5': 's',
            '7': 't',
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.encrypt_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.decrypt_map.get(char, char) for char in ciphertext)
