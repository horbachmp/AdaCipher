class VowelConsonantPairSwap:
    def __init__(self):
        self.mapping = {
            'a': 'e', 'e': 'a',
            'i': 'o', 'o': 'i',
            'u': 'u',
            'b': 'c', 'c': 'b',
            'd': 'f', 'f': 'd',
            'g': 'h', 'h': 'g',
            'j': 'k', 'k': 'j',
            'l': 'm', 'm': 'l',
            'n': 'p', 'p': 'n',
            'q': 'r', 'r': 'q',
            's': 't', 't': 's',
            'v': 'w', 'w': 'v',
            'x': 'y', 'y': 'x',
            'z': 'z',
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            lower = char.lower()
            if lower in self.mapping:
                mapped = self.mapping[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
