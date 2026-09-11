class VowelToSymbolAndSpaceToHyphenCipher:
    def __init__(self):
        self._enc_map = {
            'a': '@', 'A': '@',
            'e': '3', 'E': '3',
            'i': '!', 'I': '!',
            'o': '0', 'O': '0',
            'u': '*', 'U': '*',
            ' ': '-',
        }
        self._dec_map = {
            '@': 'a',
            '3': 'e',
            '!': 'i',
            '0': 'o',
            '*': 'u',
            '-': ' ',
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec_map.get(ch, ch) for ch in ciphertext)
