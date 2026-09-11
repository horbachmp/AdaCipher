class WordwiseReverseWithSuffix:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        parts = plaintext.split()
        out = []
        for word in parts:
            i = len(word)
            while i > 0 and not word[i - 1].isalpha():
                i -= 1
            alpha = word[:i]
            suffix = word[i:]
            if alpha:
                out.append(alpha[::-1] + "ay" + suffix)
            else:
                out.append(word)
        return " ".join(out)

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split()
        out = []
        for word in parts:
            i = len(word)
            while i > 0 and not word[i - 1].isalpha():
                i -= 1
            alpha = word[:i]
            suffix = word[i:]
            if alpha.endswith("ay") and len(alpha) >= 2:
                core = alpha[:-2]
                out.append(core[::-1] + suffix)
            else:
                out.append(word)
        return " ".join(out)
