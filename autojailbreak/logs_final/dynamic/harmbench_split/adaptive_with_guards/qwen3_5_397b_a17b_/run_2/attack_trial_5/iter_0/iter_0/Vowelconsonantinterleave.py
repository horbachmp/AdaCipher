class VowelConsonantInterleave:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def _is_alpha(self, ch: str) -> bool:
        return ch.isalpha()

    def _is_vowel(self, ch: str) -> bool:
        return ch in self.vowels

    def _transform(self, text: str) -> str:
        chars = list(text)
        result = []
        i = 0
        n = len(chars)
        while i < n:
            if i + 1 < n:
                a = chars[i]
                b = chars[i + 1]
                if self._is_alpha(a) and self._is_alpha(b):
                    if self._is_vowel(a) != self._is_vowel(b):
                        result.append(b)
                        result.append(a)
                        i += 2
                        continue
            result.append(chars[i])
            i += 1
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
