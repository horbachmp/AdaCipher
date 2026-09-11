class KeyboardRowAlternatingShift:
    def __init__(self):
        self.rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        self.pos_map = {}
        for row in self.rows:
            for i, ch in enumerate(row):
                self.pos_map[ch] = (row, i)

    def _shift_char(self, ch: str, shift_right: bool) -> str:
        lower = ch.lower()
        if lower not in self.pos_map:
            return ch
        row, idx = self.pos_map[lower]
        if shift_right:
            new_ch = row[(idx + 1) % len(row)]
        else:
            new_ch = row[(idx - 1) % len(row)]
        return new_ch.upper() if ch.isupper() else new_ch

    def encrypt(self, plaintext: str) -> str:
        out = []
        alpha_index = 0
        for ch in plaintext:
            if ch.isalpha():
                alpha_index += 1
                out.append(self._shift_char(ch, alpha_index % 2 == 1))
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        alpha_index = 0
        for ch in ciphertext:
            if ch.isalpha():
                alpha_index += 1
                out.append(self._shift_char(ch, alpha_index % 2 == 0))
            else:
                out.append(ch)
        return "".join(out)
