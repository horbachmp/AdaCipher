class FixedKeyboardRowShiftCipher:
    def __init__(self):
        self.rows = {
            "q": "qwertyuiop",
            "a": "asdfghjkl",
            "z": "zxcvbnm",
        }
        self.char_to_row = {}
        self.char_to_index = {}
        for row_key, row in self.rows.items():
            for i, ch in enumerate(row):
                self.char_to_row[ch] = row_key
                self.char_to_index[ch] = i

    def _shift_char(self, char: str, direction: int) -> str:
        lower = char.lower()
        if lower not in self.char_to_row:
            return char
        row_key = self.char_to_row[lower]
        row = self.rows[row_key]
        idx = self.char_to_index[lower]
        new_char = row[(idx + direction) % len(row)]
        return new_char.upper() if char.isupper() else new_char

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._shift_char(char, 1) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._shift_char(char, -1) for char in ciphertext)
