class HomoglyphLookalikeSubstitution:
    def __init__(self):
        self.encrypt_map = {
            'a': 'а',
            'c': 'с',
            'e': 'е',
            'o': 'о',
            'p': 'р',
            'x': 'х',
            'y': 'у',
            'A': 'А',
            'C': 'С',
            'E': 'Е',
            'O': 'О',
            'P': 'Р',
            'X': 'Х',
            'Y': 'Ү',
        }
        self.decrypt_map = {v: k for k, v in self.encrypt_map.items()}

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.encrypt_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.decrypt_map.get(char, char) for char in ciphertext)
