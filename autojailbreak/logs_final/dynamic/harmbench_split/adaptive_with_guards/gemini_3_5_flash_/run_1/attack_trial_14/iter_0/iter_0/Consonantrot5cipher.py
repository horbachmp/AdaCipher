class ConsonantRot5Cipher:
    def __init__(self):
        self.lower_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        self.upper_consonants = [c.upper() for c in self.lower_consonants]
        self.lower_map = {c: i for i, c in enumerate(self.lower_consonants)}
        self.upper_map = {c: i for i, c in enumerate(self.upper_consonants)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.lower_map:
                idx = (self.lower_map[ch] + 5) % 21
                result.append(self.lower_consonants[idx])
            elif ch in self.upper_map:
                idx = (self.upper_map[ch] + 5) % 21
                result.append(self.upper_consonants[idx])
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.lower_map:
                idx = (self.lower_map[ch] - 5) % 21
                result.append(self.lower_consonants[idx])
            elif ch in self.upper_map:
                idx = (self.upper_map[ch] - 5) % 21
                result.append(self.upper_consonants[idx])
            else:
                result.append(ch)
        return ''.join(result)
