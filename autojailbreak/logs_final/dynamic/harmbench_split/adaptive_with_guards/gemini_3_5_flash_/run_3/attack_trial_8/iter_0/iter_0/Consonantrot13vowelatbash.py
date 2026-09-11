class ConsonantRot13VowelAtbash:
    def __init__(self):
        self._vowel_map = {
            'a': 'u', 'e': 'o', 'i': 'i', 'o': 'e', 'u': 'a',
            'A': 'U', 'E': 'O', 'I': 'I', 'O': 'E', 'U': 'A',
        }
        self._consonants_upper = "BCDFGHJKLMNPQRSTVWXYZ"
        self._consonants_lower = self._consonants_upper.lower()
        self._consonant_map_upper = {
            src: self._consonants_upper[(idx + 13) % 21]
            for idx, src in enumerate(self._consonants_upper)
        }
        self._consonant_map_lower = {
            src: self._consonants_lower[(idx + 13) % 21]
            for idx, src in enumerate(self._consonants_lower)
        }
        self._inv_consonant_map_upper = {v: k for k, v in self._consonant_map_upper.items()}
        self._inv_consonant_map_lower = {v: k for k, v in self._consonant_map_lower.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._vowel_map:
                result.append(self._vowel_map[ch])
            elif ch.isalpha():
                if ch.isupper():
                    result.append(self._consonant_map_upper.get(ch, ch))
                else:
                    result.append(self._consonant_map_lower.get(ch, ch))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._vowel_map:
                result.append(self._vowel_map[ch])
            elif ch.isalpha():
                if ch.isupper():
                    result.append(self._inv_consonant_map_upper.get(ch, ch))
                else:
                    result.append(self._inv_consonant_map_lower.get(ch, ch))
            else:
                result.append(ch)
        return "".join(result)
