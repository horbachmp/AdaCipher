class VowelConsonantPairSwapCipher:
    def __init__(self):
        self.mapping = {
            'a': 'e', 'e': 'a',
            'i': 'o', 'o': 'i',
            'u': 'u',
            'b': 'c', 'c': 'b',
            'd': 'f', 'f': 'd',
            'g': 'h', 'h': 'g',
            'j': 'k', 'k': 'j',
            'l': 'm', 'm': 'l',
            'n': 'p', 'p': 'n',
            'q': 'r', 'r': 'q',
            's': 't', 't': 's',
            'v': 'w', 'w': 'v',
            'x': 'y', 'y': 'x',
            'z': 'z'
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(
            self._swap_char(char) if char.isalpha() else char
            for char in plaintext
        )

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(
            self._swap_char(char) if char.isalpha() else char
            for char in ciphertext
        )

    def _swap_char(self, char: str) -> str:
        lower = char.lower()
        mapped = self.mapping.get(lower, lower)
        return mapped.upper() if char.isupper() else mapped
