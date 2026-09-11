class KeyboardDiagonalShiftCipher:
    def __init__(self):
        self._enc_map = {
            'A': 'Z', 'B': 'Y', 'C': 'R', 'D': 'C', 'E': 'D', 'F': 'V', 'G': 'B',
            'H': 'N', 'I': 'K', 'J': 'M', 'K': 'K', 'L': 'L', 'M': 'I', 'N': 'U',
            'O': 'L', 'P': 'P', 'Q': 'A', 'R': 'F', 'S': 'X', 'T': 'G', 'U': 'J',
            'V': 'T', 'W': 'S', 'X': 'E', 'Y': 'H', 'Z': 'W'
        }
        self._dec_map = {
            'A': 'Q', 'B': 'G', 'C': 'D', 'D': 'E', 'E': 'X', 'F': 'R', 'G': 'T',
            'H': 'Y', 'I': 'M', 'J': 'U', 'K': 'K', 'L': 'L', 'M': 'J', 'N': 'H',
            'O': 'I', 'P': 'P', 'Q': 'Q', 'R': 'C', 'S': 'W', 'T': 'V', 'U': 'N',
            'V': 'F', 'W': 'Z', 'X': 'S', 'Y': 'B', 'Z': 'A'
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                mapped = self._enc_map[ch.upper()]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                mapped = self._dec_map[ch.upper()]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return ''.join(result)
