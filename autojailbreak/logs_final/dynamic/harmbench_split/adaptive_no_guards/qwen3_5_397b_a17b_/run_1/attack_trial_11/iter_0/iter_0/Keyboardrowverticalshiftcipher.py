class KeyboardRowVerticalShiftCipher:
    def __init__(self):
        lower_enc = {
            "q": "a", "w": "s", "e": "d", "r": "f", "t": "g", "y": "h", "u": "j", "i": "k", "o": "l", "p": "z",
            "a": "x", "s": "c", "d": "v", "f": "b", "g": "n", "h": "m", "j": "q", "k": "w", "l": "e",
            "z": "r", "x": "t", "c": "y", "v": "u", "b": "i", "n": "o", "m": "p",
        }
        self.enc_map = {}
        self.dec_map = {}
        for k, v in lower_enc.items():
            self.enc_map[k] = v
            self.enc_map[k.upper()] = v.upper()
            self.dec_map[v] = k
            self.dec_map[v.upper()] = k.upper()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.dec_map.get(ch, ch) for ch in ciphertext)
