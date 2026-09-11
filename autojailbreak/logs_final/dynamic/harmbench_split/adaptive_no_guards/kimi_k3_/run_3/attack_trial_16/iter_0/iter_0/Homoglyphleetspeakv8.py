class HomoglyphLeetSpeakV8:
    def __init__(self):
        self.enc_map = {
            'a': '4', 'A': '4',
            'e': '3', 'E': '3',
            'i': '1', 'I': '1',
            'o': '0', 'O': '0',
            's': '5', 'S': '5',
            't': '7', 'T': '7',
            'z': '2', 'Z': '2',
        }
        self.dec_map = {
            '4': 'a',
            '3': 'e',
            '1': 'i',
            '0': 'o',
            '5': 's',
            '7': 't',
            '2': 'z',
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.dec_map.get(ch, ch) for ch in ciphertext)
