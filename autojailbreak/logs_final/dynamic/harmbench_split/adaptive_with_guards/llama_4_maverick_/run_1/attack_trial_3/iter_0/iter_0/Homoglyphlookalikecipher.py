class HomoglyphLookalikeCipher:
    def __init__(self):
        self._enc_map = {
            'a': 'а', 'c': 'с', 'e': 'е', 'i': 'і', 'j': 'ј', 'o': 'о', 'p': 'р', 's': 'ѕ', 'x': 'х', 'y': 'у',
            'A': 'А', 'B': 'В', 'C': 'С', 'E': 'Е', 'H': 'Н', 'I': 'І', 'J': 'Ј', 'K': 'К', 'M': 'М', 'O': 'О',
            'P': 'Р', 'S': 'Ѕ', 'T': 'Т', 'X': 'Х', 'Y': 'Ү'
        }
        self._dec_map = {
            'а': 'a', 'с': 'c', 'е': 'e', 'і': 'i', 'ј': 'j', 'о': 'o', 'р': 'p', 'ѕ': 's', 'х': 'x', 'у': 'y',
            'А': 'A', 'В': 'B', 'С': 'C', 'Е': 'E', 'Н': 'H', 'І': 'I', 'Ј': 'J', 'К': 'K', 'М': 'M', 'О': 'O',
            'Р': 'P', 'Ѕ': 'S', 'Т': 'T', 'Х': 'X', 'Ү': 'Y'
        }

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self._dec_map.get(ch, ch) for ch in ciphertext)
