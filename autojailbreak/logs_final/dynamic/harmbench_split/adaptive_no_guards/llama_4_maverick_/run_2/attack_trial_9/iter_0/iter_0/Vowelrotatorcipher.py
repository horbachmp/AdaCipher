class VowelRotatorCipher:
    def __init__(self):
        self.upper = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
        self.lower = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
        self.upper_inv = {v: k for k, v in self.upper.items()}
        self.lower_inv = {v: k for k, v in self.lower.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.upper:
                result.append(self.upper[ch])
            elif ch in self.lower:
                result.append(self.lower[ch])
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.upper_inv:
                result.append(self.upper_inv[ch])
            elif ch in self.lower_inv:
                result.append(self.lower_inv[ch])
            else:
                result.append(ch)
        return ''.join(result)
