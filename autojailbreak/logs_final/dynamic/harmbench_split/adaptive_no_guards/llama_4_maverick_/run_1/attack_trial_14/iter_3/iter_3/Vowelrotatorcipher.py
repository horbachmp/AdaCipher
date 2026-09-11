class VowelRotatorCipher:
    def __init__(self):
        self._lower = "aeiou"
        self._upper = "AEIOU"
        self._enc_lower = {self._lower[i]: self._lower[(i + 1) % 5] for i in range(5)}
        self._enc_upper = {self._upper[i]: self._upper[(i + 1) % 5] for i in range(5)}
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
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._dec_lower:
                result.append(self._dec_lower[ch])
            elif ch in self._dec_upper:
                result.append(self._dec_upper[ch])
            else:
                result.append(ch)
        return "".join(result)
