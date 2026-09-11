class ConsonantShiftCipher:
    def __init__(self):
        self._enc_map = {
            'b': 'c', 'c': 'd', 'd': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'j': 'k',
            'k': 'l', 'l': 'm', 'm': 'n', 'n': 'p', 'p': 'q', 'q': 'r', 'r': 's',
            's': 't', 't': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'b',
            'B': 'C', 'C': 'D', 'D': 'F', 'F': 'G', 'G': 'H', 'H': 'J', 'J': 'K',
            'K': 'L', 'L': 'M', 'M': 'N', 'N': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S',
            'S': 'T', 'T': 'V', 'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'B',
        }
        self._dec_map = {
            'b': 'z', 'c': 'b', 'd': 'c', 'f': 'd', 'g': 'f', 'h': 'g', 'j': 'h',
            'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'p': 'n', 'q': 'p', 'r': 'q',
            's': 'r', 't': 's', 'v': 't', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y',
            'B': 'Z', 'C': 'B', 'D': 'C', 'F': 'D', 'G': 'F', 'H': 'G', 'J': 'H',
            'K': 'J', 'L': 'K', 'M': 'L', 'N': 'M', 'P': 'N', 'Q': 'P', 'R': 'Q',
            'S': 'R', 'T': 'S', 'V': 'T', 'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Y',
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            result.append(self._enc_map.get(ch, ch))
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            result.append(self._dec_map.get(ch, ch))
        return ''.join(result)
