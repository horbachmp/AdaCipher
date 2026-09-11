class ConsonantRot13VowelAtbash:
    def __init__(self):
        self.consonant_map = {
            'b': 'n', 'c': 'p', 'd': 'q', 'f': 'r', 'g': 's',
            'h': 't', 'j': 'v', 'k': 'w', 'l': 'x', 'm': 'y',
            'n': 'z', 'p': 'b', 'q': 'c', 'r': 'd', 's': 'f',
            't': 'g', 'v': 'h', 'w': 'j', 'x': 'k', 'y': 'l',
            'z': 'm'
        }
        self.vowel_map = {
            'a': 'u', 'e': 'o', 'i': 'i', 'o': 'e', 'u': 'a'
        }

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.lower() in self.consonant_map:
                mapped = self.consonant_map[ch.lower()]
                result.append(mapped.upper() if ch.isupper() else mapped)
            elif ch.lower() in self.vowel_map:
                mapped = self.vowel_map[ch.lower()]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        reverse_consonant_map = {v: k for k, v in self.consonant_map.items()}
        result = []
        for ch in ciphertext:
            if ch.lower() in reverse_consonant_map:
                mapped = reverse_consonant_map[ch.lower()]
                result.append(mapped.upper() if ch.isupper() else mapped)
            elif ch.lower() in self.vowel_map:
                mapped = self.vowel_map[ch.lower()]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return ''.join(result)
