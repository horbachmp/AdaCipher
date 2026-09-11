class QwertyShiftCipher:
    def __init__(self):
        self.rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        self.encrypt_map = {}
        self.decrypt_map = {}
        for row in self.rows:
            n = len(row)
            for i, ch in enumerate(row):
                left = row[(i - 1) % n]
                right = row[(i + 1) % n]
                self.encrypt_map[ch] = left
                self.decrypt_map[ch] = right
                self.encrypt_map[ch.upper()] = left.upper()
                self.decrypt_map[ch.upper()] = right.upper()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.encrypt_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.decrypt_map.get(ch, ch) for ch in ciphertext)
