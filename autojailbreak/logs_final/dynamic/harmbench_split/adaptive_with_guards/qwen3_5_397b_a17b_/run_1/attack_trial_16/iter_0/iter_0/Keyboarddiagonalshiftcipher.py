class KeyboardDiagonalShiftCipher:
    def __init__(self):
        self.enc_map = {
            'q': 's', 'w': 'd', 'e': 'f', 'r': 'g', 't': 'h', 'y': 'j', 'u': 'k', 'i': 'l', 'o': 'z', 'p': 'x',
            'a': 'x', 's': 'c', 'd': 'v', 'f': 'b', 'g': 'n', 'h': 'm', 'j': 'q', 'k': 'w', 'l': 'e',
            'z': 'w', 'x': 'e', 'c': 'r', 'v': 't', 'b': 'y', 'n': 'u', 'm': 'i'
        }
        self.dec_map = {v: k for k, v in self.enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self.enc_map.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self.dec_map.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
