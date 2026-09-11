class HomoglyphLookalikeSubstitution:
    def __init__(self):
        self._enc = {
            'a': 'а',
            'c': 'с',
            'e': 'е',
            'i': 'і',
            'j': 'ј',
            'o': 'о',
            'p': 'р',
            's': 'ѕ',
            'x': 'х',
            'y': 'у',
            'A': 'А',
            'B': 'В',
            'C': 'С',
            'E': 'Е',
            'H': 'Н',
            'I': 'І',
            'J': 'Ј',
            'K': 'К',
            'M': 'М',
            'O': 'О',
            'P': 'Р',
            'S': 'Ѕ',
            'T': 'Т',
            'X': 'Х',
            'Y': 'Ү',
        }
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec.get(ch, ch) for ch in ciphertext)
