class FixedKeyboardRowShiftLeftCipher:
    def __init__(self):
        self._rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        self._enc_map = {}
        self._dec_map = {}
        for row in self._rows:
            n = len(row)
            for i, ch in enumerate(row):
                left = row[i - 1]
                right = row[(i + 1) % n]
                self._enc_map[ch] = left
                self._dec_map[ch] = right

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            low = ch.lower()
            if low in self._enc_map and ch.isalpha():
                mapped = self._enc_map[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            low = ch.lower()
            if low in self._dec_map and ch.isalpha():
                mapped = self._dec_map[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
