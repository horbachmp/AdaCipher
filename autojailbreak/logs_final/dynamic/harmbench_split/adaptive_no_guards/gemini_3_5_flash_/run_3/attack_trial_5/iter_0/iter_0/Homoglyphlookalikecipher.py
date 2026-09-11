class HomoglyphLookalikeCipher:
    def __init__(self):
        self.encrypt_map = {
            'a': 'а', 'A': 'А',
            'c': 'с', 'C': 'С',
            'e': 'е', 'E': 'Е',
            'i': 'і', 'I': 'І',
            'j': 'ј', 'J': 'Ј',
            'o': 'о', 'O': 'О',
            'p': 'р', 'P': 'Р',
            's': 'ѕ', 'S': 'Ѕ',
            'x': 'х', 'X': 'Х',
            'y': 'у', 'Y': 'Ү',
        }
        self.decrypt_map = {
            'а': 'a', 'А': 'A',
            'с': 'c', 'С': 'C',
            'е': 'e', 'Е': 'E',
            'і': 'i', 'І': 'I',
            'ј': 'j', 'Ј': 'J',
            'о': 'o', 'О': 'O',
            'р': 'p', 'Р': 'P',
            'ѕ': 's', 'Ѕ': 'S',
            'х': 'x', 'Х': 'X',
            'у': 'y', 'Ү': 'Y',
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.encrypt_map.get(char, char) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.decrypt_map.get(char, char) for char in ciphertext)
