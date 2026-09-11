class QwertyShiftCipher:
    def __init__(self):
        self._enc = {
            'q': 'w', 'w': 'e', 'e': 'r', 'r': 't', 't': 'y', 'y': 'u', 'u': 'i', 'i': 'o', 'o': 'p', 'p': 'q',
            'a': 's', 's': 'd', 'd': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'j': 'k', 'k': 'l', 'l': 'a',
            'z': 'x', 'x': 'c', 'c': 'v', 'v': 'b', 'b': 'n', 'n': 'm', 'm': 'z',
        }
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            lower = ch.lower()
            if lower in self._enc:
                mapped = self._enc[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            lower = ch.lower()
            if lower in self._dec:
                mapped = self._dec[lower]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
