class BoustrophedonWordReversal:
    def __init__(self):
        pass

    def _split_sentences(self, text: str):
        sentences = []
        start = 0
        for i, ch in enumerate(text):
            if ch in ".!?":
                sentences.append((text[start:i].strip(), ch))
                start = i + 1
        if start < len(text):
            tail = text[start:].strip()
            if tail:
                sentences.append((tail, ""))
        return sentences

    def encrypt(self, plaintext: str) -> str:
        out = []
        for sentence, punct in self._split_sentences(plaintext):
            if not sentence:
                out.append(punct)
                continue
            words = sentence.split()
            words = list(reversed(words))
            for i in range(1, len(words), 2):
                words[i] = words[i][::-1]
            out.append(" ".join(words) + punct)
        return " ".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for sentence, punct in self._split_sentences(ciphertext):
            if not sentence:
                out.append(punct)
                continue
            words = sentence.split()
            for i in range(1, len(words), 2):
                words[i] = words[i][::-1]
            words = list(reversed(words))
            out.append(" ".join(words) + punct)
        return " ".join(out)
