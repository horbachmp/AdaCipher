class HomoglyphLeetSpeakV9:
    def __init__(self):
        self._encrypt_map = {
            'a': '4', 'A': '4',
            'e': '3', 'E': '3',
            'i': '1', 'I': '1',
            'o': '0', 'O': '0',
            's': '5', 'S': '5',
            't': '7', 'T': '7',
            'h': '8', 'H': '8',
        }
        self._decrypt_map = {
            '4': 'a',
            '3': 'e',
            '1': 'i',
            '0': 'o',
            '5': 's',
            '7': 't',
            '8': 'h',
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._encrypt_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._decrypt_map.get(char, char) for char in ciphertext)
