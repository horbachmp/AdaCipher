class KeyboardRowShiftLeftWithCasePreservation:
    def __init__(self):
        self.rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        self.left_map = {}
        self.right_map = {}
        for row in self.rows:
            for i, ch in enumerate(row):
                self.left_map[ch] = row[(i - 1) % len(row)]
                self.right_map[ch] = row[(i + 1) % len(row)]

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self.left_map.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self.right_map.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
