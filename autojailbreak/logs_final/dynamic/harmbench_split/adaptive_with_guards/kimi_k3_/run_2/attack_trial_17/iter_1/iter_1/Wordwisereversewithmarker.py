class WordwiseReverseWithMarker:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        words = plaintext.split(" ")
        out = []
        for word in words:
            i = len(word)
            while i > 0 and not word[i - 1].isalnum():
                i -= 1
            core = word[:i]
            punct = word[i:]
            if core:
                out.append(core[::-1] + "*" + punct)
            else:
                out.append(word)
        return " ".join(out)

    def decrypt(self, ciphertext: str) -> str:
        words = ciphertext.split(" ")
        out = []
        for word in words:
            i = len(word)
            while i > 0 and not word[i - 1].isalnum():
                i -= 1
            core = word[:i]
            punct = word[i:]
            if core.endswith("*"):
                core = core[:-1]
                out.append(core[::-1] + punct)
            else:
                out.append(word)
        return " ".join(out)
