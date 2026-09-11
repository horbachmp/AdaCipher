class VowelConsonantInterchangeCipher:
    def __init__(self):
        self.vowel_encrypt = {
            'a': 'u', 'e': 'o', 'i': 'i', 'o': 'e', 'u': 'a'
        }
        self.vowel_decrypt = {
            'u': 'a', 'o': 'e', 'i': 'i', 'e': 'o', 'a': 'u'
        }
        self.consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        self.consonant_index = {ch: i for i, ch in enumerate(self.consonants)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if not char.isalpha():
                result.append(char)
                continue
            lower = char.lower()
            if lower in self.vowel_encrypt:
                mapped = self.vowel_encrypt[lower]
            else:
                idx = self.consonant_index[lower]
                mapped = self.consonants[(idx + 13) % 21]
            result.append(mapped.upper() if char.isupper() else mapped)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if not char.isalpha():
                result.append(char)
                continue
            lower = char.lower()
            if lower in self.vowel_decrypt:
                mapped = self.vowel_decrypt[lower]
            else:
                idx = self.consonant_index[lower]
                mapped = self.consonants[(idx + 8) % 21]
            result.append(mapped.upper() if char.isupper() else mapped)
        return "".join(result)
