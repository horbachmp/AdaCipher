class ConsonantRot13Cipher:
    def __init__(self):
        self.lower = "bcdfghjklmnpqrstvwxyz"
        self.upper = "BCDFGHJKLMNPQRSTVWXYZ"
        self.lower_map = {c: i for i, c in enumerate(self.lower)}
        self.upper_map = {c: i for i, c in enumerate(self.upper)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char in self.lower_map:
                idx = self.lower_map[char]
                result.append(self.lower[(idx + 13) % 21])
            elif char in self.upper_map:
                idx = self.upper_map[char]
                result.append(self.upper[(idx + 13) % 21])
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char in self.lower_map:
                idx = self.lower_map[char]
                result.append(self.lower[(idx - 13) % 21])
            elif char in self.upper_map:
                idx = self.upper_map[char]
                result.append(self.upper[(idx - 13) % 21])
            else:
                result.append(char)
        return "".join(result)
