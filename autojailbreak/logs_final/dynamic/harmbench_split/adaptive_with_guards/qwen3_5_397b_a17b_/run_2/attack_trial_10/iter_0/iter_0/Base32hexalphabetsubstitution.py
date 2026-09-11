class Base32HexAlphabetSubstitution:
    def __init__(self):
        self._enc_upper = {
            **{chr(ord('A') + i): str(i) for i in range(10)},
            **{chr(ord('A') + 10 + i): chr(ord('A') + i) for i in range(16)}
        }
        self._enc_lower = {
            **{chr(ord('a') + i): str(i) for i in range(10)},
            **{chr(ord('a') + 10 + i): chr(ord('a') + i) for i in range(16)}
        }
        self._dec_upper = {v: k for k, v in self._enc_upper.items()}
        self._dec_lower = {v: k for k, v in self._enc_lower.items()}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch in self._enc_upper:
                out.append(self._enc_upper[ch])
            elif ch in self._enc_lower:
                out.append(self._enc_lower[ch])
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch in self._dec_upper:
                out.append(self._dec_upper[ch])
            elif ch in self._dec_lower:
                out.append(self._dec_lower[ch])
            else:
                out.append(ch)
        return "".join(out)
