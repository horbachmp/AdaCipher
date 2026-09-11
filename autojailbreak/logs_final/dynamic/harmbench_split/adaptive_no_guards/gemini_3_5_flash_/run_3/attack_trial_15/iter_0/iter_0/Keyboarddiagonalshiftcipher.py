class KeyboardDiagonalShiftCipher:
    def __init__(self):
        self.encrypt_map = {
            'q': 'a', 'w': 's', 'e': 'd', 'r': 'f', 't': 'g', 'y': 'h', 'u': 'j', 'i': 'k', 'o': 'l', 'p': 'z',
            'a': 'x', 's': 'c', 'd': 'v', 'f': 'b', 'g': 'n', 'h': 'm', 'j': 'q', 'k': 'w', 'l': 'e',
            'z': 'r', 'x': 't', 'c': 'y', 'v': 'u', 'b': 'i', 'n': 'o', 'm': 'p'
        }
        self.decrypt_map = {v: k for k, v in self.encrypt_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            lower = char.lower()
            if lower in self.encrypt_map:
                mapped = self.encrypt_map[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            lower = char.lower()
            if lower in self.decrypt_map:
                mapped = self.decrypt_map[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return "".join(result)
