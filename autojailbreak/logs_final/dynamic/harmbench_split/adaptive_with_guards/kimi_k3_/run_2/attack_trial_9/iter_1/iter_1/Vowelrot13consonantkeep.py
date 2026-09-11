class VowelRot13ConsonantKeep:
    def __init__(self):
        self._enc_lower = {'a': 'i', 'e': 'o', 'i': 'u', 'o': 'a', 'u': 'e'}
        self._enc_upper = {'A': 'I', 'E': 'O', 'I': 'U', 'O': 'A', 'U': 'E'}
        self._dec_lower = {v: k for k, v in self._enc_lower.items()}
        self._dec_upper = {v: k for k, v in self._enc_upper.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._enc_lower:
                result.append(self._enc_lower[ch])
            elif ch in self._enc_upper:
                result.append(self._enc_upper[ch])
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._dec_lower:
                result.append(self._dec_lower[ch])
            elif ch in self._dec_upper:
                result.append(self._dec_upper[ch])
            else:
                result.append(ch)
        return ''.join(result)
