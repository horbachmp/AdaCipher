class ConsonantVowelPairSwap:
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
                chars = list(word)
                for k in range(0, len(chars) - 1, 2):
                    chars[k], chars[k + 1] = chars[k + 1], chars[k]
                result.append("".join(chars))
                i = j
            else:
                result.append(text[i])
                i += 1
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
