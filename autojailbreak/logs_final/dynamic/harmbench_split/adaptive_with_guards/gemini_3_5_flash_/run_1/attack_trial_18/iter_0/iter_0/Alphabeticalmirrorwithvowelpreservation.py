class AlphabeticalMirrorWithVowelPreservation:
    def __init__(self):
        self._upper_map = {
            'B': 'Z', 'C': 'Y', 'D': 'X', 'F': 'W', 'G': 'V', 'H': 'T', 'J': 'S',
            'K': 'R', 'L': 'Q', 'M': 'P', 'N': 'N', 'P': 'M', 'Q': 'L', 'R': 'K',
            'S': 'J', 'T': 'H', 'V': 'F', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'G'
        }
        self._lower_map = {
            'b': 'z', 'c': 'y', 'd': 'x', 'f': 'w', 'g': 'v', 'h': 't', 'j': 's',
            'k': 'r', 'l': 'q', 'm': 'p', 'n': 'n', 'p': 'm', 'q': 'l', 'r': 'k',
            's': 'j', 't': 'h', 'v': 'f', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'g'
        }
        self._vowels = set("AEIOUaeiou")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._vowels:
                result.append(ch)
            elif ch in self._upper_map:
                result.append(self._upper_map[ch])
            elif ch in self._lower_map:
                result.append(self._lower_map[ch])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
