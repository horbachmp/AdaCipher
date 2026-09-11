class FixedVowelConsonantMirrorCipher:
    def __init__(self):
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        vowel_map = {
            "a": "u", "e": "o", "i": "i", "o": "e", "u": "a"
        }
        consonant_map = {}
        for i, ch in enumerate(consonants):
            consonant_map[ch] = consonants[-1 - i]
        self._map = {}
        self._map.update(vowel_map)
        self._map.update(consonant_map)

    def _transform(self, text: str) -> str:
        result = []
        for ch in text:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._map.get(lower, lower)
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
