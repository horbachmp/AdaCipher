class FixedKeyboardRowInterchange:
    def __init__(self):
        upper_map = {
            "Q": "A", "A": "Q",
            "W": "S", "S": "W",
            "E": "D", "D": "E",
            "R": "F", "F": "R",
            "T": "G", "G": "T",
            "Y": "H", "H": "Y",
            "U": "J", "J": "U",
            "I": "K", "K": "I",
            "O": "L", "L": "O",
        }
        self._map = {}
        for k, v in upper_map.items():
            self._map[k] = v
            self._map[k.lower()] = v.lower()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._map.get(ch, ch) for ch in ciphertext)
