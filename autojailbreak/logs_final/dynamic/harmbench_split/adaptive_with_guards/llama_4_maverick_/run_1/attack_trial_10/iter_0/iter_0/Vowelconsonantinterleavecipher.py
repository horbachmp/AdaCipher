class VowelConsonantInterleaveCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def encrypt(self, plaintext: str) -> str:
        words = plaintext.split(" ")
        out_words = []
        for word in words:
            prefix = []
            suffix = []
            punctuation = []
            for ch in word:
                if ch.isalpha():
                    if ch in self.vowels:
                        prefix.append(ch)
                    else:
                        suffix.append(ch)
                else:
                    punctuation.append(ch)
            out_words.append("".join(prefix + suffix + punctuation))
        return " ".join(out_words)

    def decrypt(self, ciphertext: str) -> str:
        words = ciphertext.split(" ")
        out_words = []
        for word in words:
            prefix = []
            suffix = []
            punctuation = []
            for ch in word:
                if ch.isalpha():
                    if ch in self.vowels:
                        prefix.append(ch)
                    else:
                        suffix.append(ch)
                else:
                    punctuation.append(ch)
            out_words.append("".join(prefix + suffix + punctuation))
        return " ".join(out_words)
