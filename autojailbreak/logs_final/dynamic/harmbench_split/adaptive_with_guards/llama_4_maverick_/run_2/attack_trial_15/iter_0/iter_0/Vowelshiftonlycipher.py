class VowelShiftOnlyCipher:
    def __init__(self):
        self.lower_encrypt = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
        self.lower_decrypt = {'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o', 'a': 'u'}
        self.upper_encrypt = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
        self.upper_decrypt = {'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O', 'A': 'U'}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.lower_encrypt:
                result.append(self.lower_encrypt[ch])
            elif ch in self.upper_encrypt:
                result.append(self.upper_encrypt[ch])
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.lower_decrypt:
                result.append(self.lower_decrypt[ch])
            elif ch in self.upper_decrypt:
                result.append(self.upper_decrypt[ch])
            else:
                result.append(ch)
        return ''.join(result)
