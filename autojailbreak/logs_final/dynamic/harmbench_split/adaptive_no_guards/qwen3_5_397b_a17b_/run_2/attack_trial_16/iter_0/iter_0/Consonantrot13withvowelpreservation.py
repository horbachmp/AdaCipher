class ConsonantRot13WithVowelPreservation:
    def __init__(self):
        self.lower_consonants = "bcdfghjklmnpqrstvwxyz"
        self.upper_consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self.vowels = set("AEIOUaeiou")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.vowels:
                result.append(ch)
            elif ch in self.lower_consonants:
                idx = self.lower_consonants.index(ch)
                result.append(self.lower_consonants[(idx + 13) % 21])
            elif ch in self.upper_consonants:
                idx = self.upper_consonants.index(ch)
                result.append(self.upper_consonants[(idx + 13) % 21])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.vowels:
                result.append(ch)
            elif ch in self.lower_consonants:
                idx = self.lower_consonants.index(ch)
                result.append(self.lower_consonants[(idx + 8) % 21])
            elif ch in self.upper_consonants:
                idx = self.upper_consonants.index(ch)
                result.append(self.upper_consonants[(idx + 8) % 21])
            else:
                result.append(ch)
        return "".join(result)
