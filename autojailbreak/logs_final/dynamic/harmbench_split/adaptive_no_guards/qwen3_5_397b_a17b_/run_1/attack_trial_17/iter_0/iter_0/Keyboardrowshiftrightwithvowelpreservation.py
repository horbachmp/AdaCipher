class KeyboardRowShiftRightWithVowelPreservation:
    def __init__(self):
        self.rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        self.char_to_row = {}
        self.char_to_index = {}
        for row in self.rows:
            for i, ch in enumerate(row):
                self.char_to_row[ch] = row
                self.char_to_index[ch] = i
        self.vowels = set("aeiouAEIOU")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if not ch.isalpha() or ch in self.vowels:
                result.append(ch)
                continue
            lower = ch.lower()
            row = self.char_to_row.get(lower)
            if row is None:
                result.append(ch)
                continue
            idx = self.char_to_index[lower]
            shifted = row[(idx + 1) % len(row)]
            result.append(shifted.upper() if ch.isupper() else shifted)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if not ch.isalpha() or ch in self.vowels:
                result.append(ch)
                continue
            lower = ch.lower()
            row = self.char_to_row.get(lower)
            if row is None:
                result.append(ch)
                continue
            idx = self.char_to_index[lower]
            shifted = row[(idx - 1) % len(row)]
            result.append(shifted.upper() if ch.isupper() else shifted)
        return "".join(result)
