class ConsonantRot13VowelPreservation:
    def __init__(self):
        lower_consonants = "bcdfghjklmnpqrstvwxyz"
        upper_consonants = lower_consonants.upper()
        self.encrypt_map = {}
        self.decrypt_map = {}
        for i, ch in enumerate(lower_consonants):
            mapped = lower_consonants[(i + 13) % 21]
            self.encrypt_map[ch] = mapped
            self.decrypt_map[mapped] = ch
        for i, ch in enumerate(upper_consonants):
            mapped = upper_consonants[(i + 13) % 21]
            self.encrypt_map[ch] = mapped
            self.decrypt_map[mapped] = ch

    def encrypt(self, plaintext: str) -> str:
        vowels = set("aeiouAEIOU")
        result = []
        for char in plaintext:
            if char in vowels:
                result.append(char)
            elif char.isalpha():
                result.append(self.encrypt_map.get(char, char))
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        vowels = set("aeiouAEIOU")
        result = []
        for char in ciphertext:
            if char in vowels:
                result.append(char)
            elif char.isalpha():
                result.append(self.decrypt_map.get(char, char))
            else:
                result.append(char)
        return "".join(result)
