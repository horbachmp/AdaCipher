class VowelConsonantInterleaveCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def _transform(self, text: str) -> str:
        chars = list(text)
        i = 0
        while i < len(chars) - 1:
            a = chars[i]
            b = chars[i + 1]
            if a.isalpha() and b.isalpha():
                a_is_vowel = a in self.vowels
                b_is_vowel = b in self.vowels
                if a_is_vowel != b_is_vowel:
                    chars[i], chars[i + 1] = chars[i + 1], chars[i]
                    i += 2
                    continue
            i += 1
        return "".join(chars)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
