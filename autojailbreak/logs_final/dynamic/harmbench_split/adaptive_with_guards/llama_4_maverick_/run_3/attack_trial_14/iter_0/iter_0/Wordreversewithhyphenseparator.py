class WordReverseWithHyphenSeparator:
    def __init__(self):
        pass

    def _reverse_word(self, word: str) -> str:
        i = len(word)
        while i > 0 and not word[i - 1].isalnum():
            i -= 1
        core = word[:i]
        punct = word[i:]
        return core[::-1] + punct

    def encrypt(self, plaintext: str) -> str:
        words = plaintext.split(" ")
        return "-".join(self._reverse_word(word) for word in words)

    def decrypt(self, ciphertext: str) -> str:
        words = ciphertext.split("-")
        return " ".join(self._reverse_word(word) for word in words)
