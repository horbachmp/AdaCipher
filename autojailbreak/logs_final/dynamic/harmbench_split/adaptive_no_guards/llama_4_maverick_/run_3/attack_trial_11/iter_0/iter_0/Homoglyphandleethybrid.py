class HomoglyphAndLeetHybrid:
    def __init__(self):
        self._enc_map = {
            'a': 'а',
            'e': 'е',
            'o': 'о',
            'i': '1',
            't': '7',
        }
        self._dec_map = {
            'а': 'a',
            'е': 'e',
            'о': 'o',
            '1': 'i',
            '7': 't',
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec_map.get(ch, ch) for ch in ciphertext)
