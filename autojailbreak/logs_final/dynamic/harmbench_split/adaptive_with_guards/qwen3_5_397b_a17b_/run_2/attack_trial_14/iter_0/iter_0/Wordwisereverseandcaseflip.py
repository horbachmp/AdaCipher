class WordWiseReverseAndCaseFlip:
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
                word = text[i:j][::-1]
                flipped = []
                for ch in word:
                    if ch.islower():
                        flipped.append(ch.upper())
                    else:
                        flipped.append(ch.lower())
                result.append("".join(flipped))
                i = j
            else:
                result.append(text[i])
                i += 1
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
