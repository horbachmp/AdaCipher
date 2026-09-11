class FixedKeywordSubstitutionCipher:
    def __init__(self):
        keyword = "CIPHER"
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        seen = set()
        cipher_lower = []
        for ch in keyword.lower():
            if ch.isalpha() and ch not in seen:
                seen.add(ch)
                cipher_lower.append(ch)
        for ch in alphabet:
            if ch not in seen:
                seen.add(ch)
                cipher_lower.append(ch)
        self._plain_lower = alphabet
        self._cipher_lower = "".join(cipher_lower)
        self._enc_lower = {p: c for p, c in zip(self._plain_lower, self._cipher_lower)}
        self._dec_lower = {c: p for p, c in zip(self._plain_lower, self._cipher_lower)}
        self._enc_upper = {p.upper(): c.upper() for p, c in self._enc_lower.items()}
        self._dec_upper = {c.upper(): p.upper() for p, c in self._dec_lower.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.islower() and ch in self._enc_lower:
                result.append(self._enc_lower[ch])
            elif ch.isupper() and ch in self._enc_upper:
                result.append(self._enc_upper[ch])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.islower() and ch in self._dec_lower:
                result.append(self._dec_lower[ch])
            elif ch.isupper() and ch in self._dec_upper:
                result.append(self._dec_upper[ch])
            else:
                result.append(ch)
        return "".join(result)
