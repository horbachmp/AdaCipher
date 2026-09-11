class ConsonantVowelInterleaveTransposition:
    def __init__(self):
        pass

    def _transform(self, text: str, encrypting: bool) -> str:
        result = []
        word = []

        def flush():
            if not word:
                return
            token = ''.join(word)
            if len(token) >= 3 and token.isalpha():
                if encrypting:
                    result.append(token[1:] + token[0])
                else:
                    result.append(token[-1] + token[:-1])
            else:
                result.append(token)
            word.clear()

        for ch in text:
            if ch.isalpha():
                word.append(ch)
            else:
                flush()
                result.append(ch)
        flush()
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext, True)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext, False)
