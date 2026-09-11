class ReverseWordOrderCipher:
    def __init__(self):
        pass

    def _split_sentences(self, text: str):
        sentences = []
        start = 0
        for i, ch in enumerate(text):
            if ch in ".!?":
                sentences.append((text[start:i], ch))
                start = i + 1
        if start < len(text):
            sentences.append((text[start:], ""))
        return sentences

    def _transform_sentence(self, body: str, punctuation: str, encrypting: bool) -> str:
        stripped = body.strip()
        if not stripped:
            return punctuation

        words = stripped.split()
        words.reverse()
        if words:
            words[0] = words[0][:1].upper() + words[0][1:]
            if len(words) > 1:
                words[-1] = words[-1][:1].lower() + words[-1][1:]
        result = " ".join(words)
        return result + punctuation

    def encrypt(self, plaintext: str) -> str:
        parts = self._split_sentences(plaintext)
        return "".join(self._transform_sentence(body, punct, True) for body, punct in parts)

    def decrypt(self, ciphertext: str) -> str:
        parts = self._split_sentences(ciphertext)
        return "".join(self._transform_sentence(body, punct, False) for body, punct in parts)
