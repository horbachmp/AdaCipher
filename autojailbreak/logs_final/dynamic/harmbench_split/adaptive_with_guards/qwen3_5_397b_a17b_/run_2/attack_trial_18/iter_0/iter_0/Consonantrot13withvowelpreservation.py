class ConsonantRot13WithVowelPreservation:
    def __init__(self):
        self.upper_consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self.lower_consonants = "bcdfghjklmnpqrstvwxyz"
        self.upper_map = {c: self.upper_consonants[(i + 13) % 21] for i, c in enumerate(self.upper_consonants)}
        self.lower_map = {c: self.lower_consonants[(i + 13) % 21] for i, c in enumerate(self.lower_consonants)}
        self.upper_inv = {v: k for k, v in self.upper_map.items()}
        self.lower_inv = {v: k for k, v in self.lower_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.upper_map:
                result.append(self.upper_map[ch])
            elif ch in self.lower_map:
                result.append(self.lower_map[ch])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.upper_inv:
                result.append(self.upper_inv[ch])
            elif ch in self.lower_inv:
                result.append(self.lower_inv[ch])
            else:
                result.append(ch)
        return "".join(result)
