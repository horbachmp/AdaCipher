class LeetspeakSubstitutionCipher:
    def __init__(self):
        self._enc_map = {
            'a': '4', 'e': '3', 'g': '9', 'i': '1', 'o': '0', 's': '5', 't': '7',
            'A': '4', 'E': '3', 'G': '9', 'I': '1', 'O': '0', 'S': '5', 'T': '7',
        }
        self._dec_map = {
            '4': 'a', '3': 'e', '9': 'g', '1': 'i', '0': 'o', '5': 's', '7': 't'
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec_map.get(ch, ch) for ch in ciphertext)
