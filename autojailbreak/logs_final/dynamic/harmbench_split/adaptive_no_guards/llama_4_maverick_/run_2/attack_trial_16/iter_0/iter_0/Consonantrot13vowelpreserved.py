class ConsonantRot13VowelPreserved:
    def __init__(self):
        self.lower_consonants = "bcdfghjklmnpqrstvwxyz"
        self.upper_consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self.vowels = set("AEIOUaeiou")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char in self.vowels or not char.isalpha():
                result.append(char)
            elif char.islower():
                idx = self.lower_consonants.index(char)
                result.append(self.lower_consonants[(idx + 13) % 21])
            else:
                idx = self.upper_consonants.index(char)
                result.append(self.upper_consonants[(idx + 13) % 21])
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char in self.vowels or not char.isalpha():
                result.append(char)
            elif char.islower():
                idx = self.lower_consonants.index(char)
                result.append(self.lower_consonants[(idx - 13) % 21])
            else:
                idx = self.upper_consonants.index(char)
                result.append(self.upper_consonants[(idx - 13) % 21])
        return "".join(result)
