class VowelConsonantInterchange:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

    def _transform(self, text: str) -> str:
        result = []
        i = 0
        n = len(text)
        while i < n:
            if i + 1 < n:
                c1 = text[i]
                c2 = text[i + 1]
                if c1.isalpha() and c2.isalpha():
                    t1 = c1 in self.vowels
                    t2 = c2 in self.vowels
                    if t1 != t2:
                        result.append(c2)
                        result.append(c1)
                        i += 2
                        continue
            result.append(text[i])
            i += 1
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
