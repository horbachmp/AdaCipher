class VowelShiftConsonantKeep:
    def __init__(self):
        self._enc_lower = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
        self._dec_lower = {'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o'}
        self._enc_upper = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
        self._dec_upper = {'A': 'U', 'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O'}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch in self._enc_lower:
                out.append(self._enc_lower[ch])
            elif ch in self._enc_upper:
                out.append(self._enc_upper[ch])
            else:
                out.append(ch)
        return ''.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch in self._dec_lower:
                out.append(self._dec_lower[ch])
            elif ch in self._dec_upper:
                out.append(self._dec_upper[ch])
            else:
                out.append(ch)
        return ''.join(out)
