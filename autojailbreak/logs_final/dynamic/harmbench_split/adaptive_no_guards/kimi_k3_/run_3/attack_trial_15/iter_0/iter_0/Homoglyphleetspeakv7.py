class HomoglyphLeetSpeakV7:
    def __init__(self):
        self.encrypt_map = {
            'a': '4', 'A': '4',
            'e': '3', 'E': '3',
            'i': '1', 'I': '1',
            'o': '0', 'O': '0',
            's': '5', 'S': '5',
            't': '7', 'T': '7',
            'z': '2', 'Z': '2',
            'b': '8', 'B': '8',
        }
        self.decrypt_map = {
            '4': 'a',
            '3': 'e',
            '1': 'i',
            '0': 'o',
            '5': 's',
            '7': 't',
            '2': 'z',
            '8': 'b',
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.encrypt_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.decrypt_map.get(char, char) for char in ciphertext)
