class WordwiseFirstLastSwap:
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
                if len(word) >= 2:
                    word = word[-1] + word[1:-1] + word[0]
                result.append(word)
                i = j
            else:
                result.append(text[i])
                i += 1
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
