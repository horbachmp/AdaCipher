class AlternatingCaseVowelConsonantInversion:
    def __init__(self):
        self._vowel_map = {
            'A': 'U', 'E': 'O', 'I': 'I', 'O': 'E', 'U': 'A',
            'a': 'u', 'e': 'o', 'i': 'i', 'o': 'e', 'u': 'a'
        }
        self._consonant_map = {
            'B': 'Z', 'C': 'Y', 'D': 'X', 'F': 'W', 'G': 'V', 'H': 'T', 'J': 'S',
            'K': 'R', 'L': 'Q', 'M': 'P', 'N': 'N', 'P': 'M', 'Q': 'L', 'R': 'K',
            'S': 'J', 'T': 'H', 'V': 'G', 'W': 'F', 'X': 'D', 'Y': 'C', 'Z': 'B',
            'b': 'z', 'c': 'y', 'd': 'x', 'f': 'w', 'g': 'v', 'h': 't', 'j': 's',
            'k': 'r', 'l': 'q', 'm': 'p', 'n': 'n', 'p': 'm', 'q': 'l', 'r': 'k',
            's': 'j', 't': 'h', 'v': 'g', 'w': 'f', 'x': 'd', 'y': 'c', 'z': 'b'
        }

    def _transform(self, text: str) -> str:
        result = []
        for ch in text:
            if ch in self._vowel_map:
                result.append(self._vowel_map[ch])
            elif ch in self._consonant_map:
                result.append(self._consonant_map[ch])
            else:
                result.append(ch)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
