class KeyboardRowShiftRightWithNumberShift:
    def __init__(self):
        self.rows_lower = {
            "q": "w", "w": "e", "e": "r", "r": "t", "t": "y", "y": "u", "u": "i", "i": "o", "o": "p", "p": "q",
            "a": "s", "s": "d", "d": "f", "f": "g", "g": "h", "h": "j", "j": "k", "k": "l", "l": "a",
            "z": "x", "x": "c", "c": "v", "v": "b", "b": "n", "n": "m", "m": "z"
        }
        self.rows_upper = {k.upper(): v.upper() for k, v in self.rows_lower.items()}
        self.rows_lower_inv = {v: k for k, v in self.rows_lower.items()}
        self.rows_upper_inv = {v: k for k, v in self.rows_upper.items()}
        self.digit_enc = {str(i): str((i + 1) % 10) for i in range(10)}
        self.digit_dec = {v: k for k, v in self.digit_enc.items()}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch in self.rows_lower:
                out.append(self.rows_lower[ch])
            elif ch in self.rows_upper:
                out.append(self.rows_upper[ch])
            elif ch in self.digit_enc:
                out.append(self.digit_enc[ch])
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch in self.rows_lower_inv:
                out.append(self.rows_lower_inv[ch])
            elif ch in self.rows_upper_inv:
                out.append(self.rows_upper_inv[ch])
            elif ch in self.digit_dec:
                out.append(self.digit_dec[ch])
            else:
                out.append(ch)
        return "".join(out)
