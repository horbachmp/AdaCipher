class ReverseWordCipher:
    def __init__(self):
        pass

    def _transform(self, text: str) -> str:
        result = []
        i = 0
        n = len(text)
        while i < n:
            if text[i].isalpha():
                j = i
                while j < n and text[j].isalpha():
                    j += 1
                word = text[i:j]
                pattern = [c.isupper() for c in word]
                reversed_letters = list(reversed(word))
                transformed = []
                for idx, ch in enumerate(reversed_letters):
                    transformed.append(ch.upper() if pattern[idx] else ch.lower())
                result.append("".join(transformed))
                i = j
            else:
                result.append(text[i])
                i += 1
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
