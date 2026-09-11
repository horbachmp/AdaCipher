class VowelConsonantPairSwapCipher:
    def __init__(self):
        self._map = {
            'A': 'E', 'E': 'A',
            'I': 'O', 'O': 'I',
            'U': 'U',
            'B': 'C', 'C': 'B',
            'D': 'F', 'F': 'D',
            'G': 'H', 'H': 'G',
            'J': 'K', 'K': 'J',
            'L': 'M', 'M': 'L',
            'N': 'P', 'P': 'N',
            'Q': 'R', 'R': 'Q',
            'S': 'T', 'T': 'S',
            'V': 'W', 'W': 'V',
            'X': 'Y', 'Y': 'X',
            'Z': 'Z',
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                upper = ch.upper()
                mapped = self._map.get(upper, upper)
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
