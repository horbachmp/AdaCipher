class VowelConsonantAlternatingShift:
    def __init__(self):
        self._enc_vowels = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
        self._dec_vowels = {'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O', 'A': 'U'}
        self._enc_consonants = {
            'B': 'C', 'C': 'D', 'D': 'F', 'F': 'G', 'G': 'H', 'H': 'J', 'J': 'K',
            'K': 'L', 'L': 'M', 'M': 'N', 'N': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S',
            'S': 'T', 'T': 'V', 'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'B'
        }
        self._dec_consonants = {
            'C': 'B', 'D': 'C', 'F': 'D', 'G': 'F', 'H': 'G', 'J': 'H', 'K': 'J',
            'L': 'K', 'M': 'L', 'N': 'M', 'P': 'N', 'Q': 'P', 'R': 'Q', 'S': 'R',
            'T': 'S', 'V': 'T', 'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Y', 'B': 'Z'
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            upper = ch.upper()
            if upper in self._enc_vowels:
                mapped = self._enc_vowels[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            elif upper.isalpha():
                mapped = self._enc_consonants[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            upper = ch.upper()
            if upper in self._dec_vowels:
                mapped = self._dec_vowels[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            elif upper.isalpha():
                mapped = self._dec_consonants[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return ''.join(result)
