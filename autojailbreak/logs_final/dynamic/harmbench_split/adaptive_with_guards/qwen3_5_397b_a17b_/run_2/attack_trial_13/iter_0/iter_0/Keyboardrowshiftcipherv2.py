class KeyboardRowShiftCipherV2:
    def __init__(self):
        self._enc = {
            'q': 'p', 'w': 'q', 'e': 'w', 'r': 'e', 't': 'r', 'y': 't', 'u': 'y', 'i': 'u', 'o': 'i', 'p': 'o',
            'a': 'l', 's': 'a', 'd': 's', 'f': 'd', 'g': 'f', 'h': 'g', 'j': 'h', 'k': 'j', 'l': 'k',
            'z': 'm', 'x': 'z', 'c': 'x', 'v': 'c', 'b': 'v', 'n': 'b', 'm': 'n',
        }
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.isalpha():
                low = ch.lower()
                mapped = self._enc.get(low, low)
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return ''.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch.isalpha():
                low = ch.lower()
                mapped = self._dec.get(low, low)
                out.append(mapped.upper() if ch.isupper() else mapped)
            else:
                out.append(ch)
        return ''.join(out)
