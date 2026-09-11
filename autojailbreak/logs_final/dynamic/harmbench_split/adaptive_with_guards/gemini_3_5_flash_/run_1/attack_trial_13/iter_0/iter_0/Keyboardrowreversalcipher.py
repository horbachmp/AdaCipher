class KeyboardRowReversalCipher:
    def __init__(self):
        self._map = {}
        rows = [
            ("qwertyuiop", "poiuytrewq"),
            ("asdfghjkl", "lkjhgfdsa"),
            ("zxcvbnm", "mnbvcxz"),
        ]
        for original, reversed_row in rows:
            for a, b in zip(original, reversed_row):
                self._map[a] = b
                self._map[b] = a

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            lower = char.lower()
            if lower in self._map:
                mapped = self._map[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
