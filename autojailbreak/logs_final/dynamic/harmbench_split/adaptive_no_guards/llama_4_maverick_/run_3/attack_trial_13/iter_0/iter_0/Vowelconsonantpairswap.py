class VowelConsonantPairSwap:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def _is_alpha(self, ch: str) -> bool:
        return ch.isalpha()

    def _is_vowel(self, ch: str) -> bool:
        return ch in self.vowels

    def encrypt(self, plaintext: str) -> str:
        chars = list(plaintext)
        i = 0
        while i < len(chars) - 1:
            a, b = chars[i], chars[i + 1]
            if self._is_alpha(a) and self._is_alpha(b):
                if self._is_vowel(a) != self._is_vowel(b):
                    chars[i], chars[i + 1] = chars[i + 1], chars[i]
                    i += 2
                    continue
            i += 1
        return "".join(chars)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
