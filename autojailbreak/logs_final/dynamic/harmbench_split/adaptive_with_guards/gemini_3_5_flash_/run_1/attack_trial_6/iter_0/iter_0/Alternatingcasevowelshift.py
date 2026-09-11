class AlternatingCaseVowelShift:
    def __init__(self):
        self._lower_enc = str.maketrans({"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"})
        self._upper_enc = str.maketrans({"A": "E", "E": "I", "I": "O", "O": "U", "U": "A"})
        self._lower_dec = str.maketrans({"e": "a", "i": "e", "o": "i", "u": "o", "a": "u"})
        self._upper_dec = str.maketrans({"E": "A", "I": "E", "O": "I", "U": "O", "A": "U"})

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in "aeiou":
                result.append(ch.translate(self._lower_enc))
            elif ch in "AEIOU":
                result.append(ch.translate(self._upper_enc))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in "aeiou":
                result.append(ch.translate(self._lower_dec))
            elif ch in "AEIOU":
                result.append(ch.translate(self._upper_dec))
            else:
                result.append(ch)
        return "".join(result)
