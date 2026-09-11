class WordBoundaryReversalCipher:
    def __init__(self):
        pass

    def _tokenize(self, text: str):
        tokens = []
        current = []
        current_is_word = None
        for ch in text:
            is_word = ch.isalnum()
            if current_is_word is None or is_word == current_is_word:
                current.append(ch)
                current_is_word = is_word
            else:
                tokens.append("".join(current))
                current = [ch]
                current_is_word = is_word
        if current:
            tokens.append("".join(current))
        return tokens

    def encrypt(self, plaintext: str) -> str:
        tokens = self._tokenize(plaintext)
        return "".join(reversed(tokens))

    def decrypt(self, ciphertext: str) -> str:
        tokens = self._tokenize(ciphertext)
        return "".join(reversed(tokens))
