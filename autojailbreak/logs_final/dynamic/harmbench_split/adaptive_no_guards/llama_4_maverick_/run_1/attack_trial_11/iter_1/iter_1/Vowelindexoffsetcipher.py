class VowelIndexOffsetCipher:
    def __init__(self):
        self._lower_encrypt = {'a': 'i', 'e': 'o', 'i': 'u', 'o': 'a', 'u': 'e'}
        self._upper_encrypt = {'A': 'I', 'E': 'O', 'I': 'U', 'O': 'A', 'U': 'E'}
        self._lower_decrypt = {'a': 'o', 'e': 'u', 'i': 'a', 'o': 'e', 'u': 'i'}
        self._upper_decrypt = {'A': 'O', 'E': 'U', 'I': 'A', 'O': 'E', 'U': 'I'}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._lower_encrypt:
                result.append(self._lower_encrypt[ch])
            elif ch in self._upper_encrypt:
                result.append(self._upper_encrypt[ch])
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._lower_decrypt:
                result.append(self._lower_decrypt[ch])
            elif ch in self._upper_decrypt:
                result.append(self._upper_decrypt[ch])
            else:
                result.append(ch)
        return ''.join(result)
