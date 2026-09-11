class VowelConsonantDoubletInversion:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def _is_letter(self, ch: str) -> bool:
        return ch.isalpha()

    def _is_vowel(self, ch: str) -> bool:
        return ch in self.vowels

    def _transform(self, text: str) -> str:
        result = []
        i = 0
        n = len(text)
        while i < n:
            if i == n - 1:
                result.append(text[i])
                break
            a = text[i]
            b = text[i + 1]
            if self._is_letter(a) and self._is_letter(b):
                if (self._is_vowel(a) and not self._is_vowel(b)) or (not self._is_vowel(a) and self._is_vowel(b)):
                    result.append(b)
                    result.append(a)
                    i += 2
                    continue
            result.append(a)
            i += 1
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
