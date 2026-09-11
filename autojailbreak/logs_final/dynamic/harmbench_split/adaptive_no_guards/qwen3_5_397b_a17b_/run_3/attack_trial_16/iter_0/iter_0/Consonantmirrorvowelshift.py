class ConsonantMirrorVowelShift:
    def __init__(self):
        self.vowel_encrypt = {
            'a': 'i', 'e': 'o', 'i': 'u', 'o': 'a', 'u': 'e'
        }
        self.vowel_decrypt = {
            'i': 'a', 'o': 'e', 'u': 'i', 'a': 'o', 'e': 'u'
        }
        consonants = "bcdfghjklmnpqrstvwxyz"
        mirrored = consonants[::-1]
        self.consonant_map = {}
        for a, b in zip(consonants, mirrored):
            self.consonant_map[a] = b
            self.consonant_map[b] = a

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            lower = char.lower()
            if lower.isalpha():
                if lower in self.vowel_encrypt:
                    mapped = self.vowel_encrypt[lower]
                else:
                    mapped = self.consonant_map[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            lower = char.lower()
            if lower.isalpha():
                if lower in self.vowel_decrypt:
                    mapped = self.vowel_decrypt[lower]
                else:
                    mapped = self.consonant_map[lower]
                result.append(mapped.upper() if char.isupper() else mapped)
            else:
                result.append(char)
        return ''.join(result)
