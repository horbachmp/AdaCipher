class KeyboardRowAlternatingShiftCipher:
    def __init__(self):
        self.top = "qwertyuiop"
        self.middle = "asdfghjkl"
        self.bottom = "zxcvbnm"
        self.enc_maps = {
            "top": {c: self.top[(i + 1) % len(self.top)] for i, c in enumerate(self.top)},
            "middle": {c: self.middle[(i - 1) % len(self.middle)] for i, c in enumerate(self.middle)},
            "bottom": {c: self.bottom[(i + 1) % len(self.bottom)] for i, c in enumerate(self.bottom)},
        }
        self.dec_maps = {
            "top": {c: self.top[(i - 1) % len(self.top)] for i, c in enumerate(self.top)},
            "middle": {c: self.middle[(i + 1) % len(self.middle)] for i, c in enumerate(self.middle)},
            "bottom": {c: self.bottom[(i - 1) % len(self.bottom)] for i, c in enumerate(self.bottom)},
        }

    def _row(self, ch: str):
        c = ch.lower()
        if c in self.top:
            return "top"
        if c in self.middle:
            return "middle"
        if c in self.bottom:
            return "bottom"
        return None

    def _transform(self, text: str, mapping_set) -> str:
        out = []
        for ch in text:
            row = self._row(ch)
            if row is None:
                out.append(ch)
                continue
            lower = ch.lower()
            mapped = mapping_set[row][lower]
            out.append(mapped.upper() if ch.isupper() else mapped)
        return "".join(out)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext, self.enc_maps)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext, self.dec_maps)
