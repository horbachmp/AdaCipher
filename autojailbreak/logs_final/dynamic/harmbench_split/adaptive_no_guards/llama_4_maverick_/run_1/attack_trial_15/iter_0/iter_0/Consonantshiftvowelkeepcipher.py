class ConsonantShiftVowelKeepCipher:
    def __init__(self):
        self.lower_consonants = "bcdfghjklmnpqrstvwxyz"
        self.upper_consonants = self.lower_consonants.upper()
        self.lower_map_enc = {c: self.lower_consonants[(i + 1) % len(self.lower_consonants)] for i, c in enumerate(self.lower_consonants)}
        self.upper_map_enc = {c: self.upper_consonants[(i + 1) % len(self.upper_consonants)] for i, c in enumerate(self.upper_consonants)}
        self.lower_map_dec = {c: self.lower_consonants[(i - 1) % len(self.lower_consonants)] for i, c in enumerate(self.lower_consonants)}
        self.upper_map_dec = {c: self.upper_consonants[(i - 1) % len(self.upper_consonants)] for i, c in enumerate(self.upper_consonants)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.lower_map_enc:
                result.append(self.lower_map_enc[ch])
            elif ch in self.upper_map_enc:
                result.append(self.upper_map_enc[ch])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.lower_map_dec:
                result.append(self.lower_map_dec[ch])
            elif ch in self.upper_map_dec:
                result.append(self.upper_map_dec[ch])
            else:
                result.append(ch)
        return "".join(result)
