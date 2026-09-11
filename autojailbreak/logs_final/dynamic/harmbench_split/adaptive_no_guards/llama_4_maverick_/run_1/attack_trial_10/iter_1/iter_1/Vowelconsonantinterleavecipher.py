class VowelConsonantInterleaveCipher:
    def __init__(self):
        pass

    def _swap_word(self, word: str) -> str:
        chars = list(word)
        for i in range(0, len(chars) - 1, 2):
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
        return "".join(chars)

    def _transform(self, text: str) -> str:
        result = []
        current = []
        for ch in text:
            if ch.isalpha():
                current.append(ch)
            else:
                if current:
                    result.append(self._swap_word("".join(current)))
                    current = []
                result.append(ch)
        if current:
            result.append(self._swap_word("".join(current)))
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
