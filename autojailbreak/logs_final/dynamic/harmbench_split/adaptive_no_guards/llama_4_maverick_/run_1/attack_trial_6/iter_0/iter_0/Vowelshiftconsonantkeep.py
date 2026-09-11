class VowelShiftConsonantKeep:
    def __init__(self):
        self._enc_lower = str.maketrans({"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"})
        self._enc_upper = str.maketrans({"A": "E", "E": "I", "I": "O", "O": "U", "U": "A"})
        self._dec_lower = str.maketrans({"a": "u", "e": "a", "i": "e", "o": "i", "u": "o"})
        self._dec_upper = str.maketrans({"A": "U", "E": "A", "I": "E", "O": "I", "U": "O"})

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in "aeiou":
                result.append(ch.translate(self._enc_lower))
            elif ch in "AEIOU":
                result.append(ch.translate(self._enc_upper))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in "aeiou":
                result.append(ch.translate(self._dec_lower))
            elif ch in "AEIOU":
                result.append(ch.translate(self._dec_upper))
            else:
                result.append(ch)
        return "".join(result)
