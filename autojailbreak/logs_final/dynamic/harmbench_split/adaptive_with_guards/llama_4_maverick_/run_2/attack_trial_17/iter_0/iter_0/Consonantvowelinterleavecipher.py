class ConsonantVowelInterleaveCipher:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)

    def _transform(self, text: str) -> str:
        chars = list(text)
        i = 0
        n = len(chars)
        while i < n - 1:
            a = chars[i]
            b = chars[i + 1]
            if a.isalpha() and b.isalpha():
                a_vowel = a in self.vowels
                b_vowel = b in self.vowels
                if a_vowel != b_vowel:
                    chars[i], chars[i + 1] = b, a
                    i += 2
                    continue
            i += 1
        return "".join(chars)
