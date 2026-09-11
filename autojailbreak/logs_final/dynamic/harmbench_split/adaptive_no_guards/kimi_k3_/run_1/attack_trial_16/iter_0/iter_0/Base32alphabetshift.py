class Base32AlphabetShift:
    def __init__(self):
        self.encrypt_map = {
            'a': 'A1', 'b': 'B2', 'c': 'C3', 'd': 'D4', 'e': 'E5', 'f': 'F6', 'g': 'G7', 'h': 'H8', 'i': 'I9', 'j': 'J0',
            'k': 'K1', 'l': 'L2', 'm': 'M3', 'n': 'N4', 'o': 'O5', 'p': 'P6', 'q': 'Q7', 'r': 'R8', 's': 'S9', 't': 'T0',
            'u': 'U1', 'v': 'V2', 'w': 'W3', 'x': 'X4', 'y': 'Y5', 'z': 'Z6'
        }
        self.decrypt_map = {v: k for k, v in self.encrypt_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                result.append(self.encrypt_map[ch.lower()])
            elif ch == ' ':
                result.append('--')
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        while i < len(ciphertext):
            if ciphertext.startswith('--', i):
                result.append(' ')
                i += 2
            elif i + 1 < len(ciphertext) and ciphertext[i].isalpha() and ciphertext[i + 1].isdigit():
                pair = ciphertext[i:i + 2]
                result.append(self.decrypt_map.get(pair, pair[0]))
                i += 2
            else:
                result.append(ciphertext[i])
                i += 1
        return ''.join(result)
