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
            core = word[:i]
            suffix = word[i:]
            if core and any(ch.isalpha() for ch in core):
                out.append(core[::-1] + "ay" + suffix)
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
            core = word[:i]
            suffix = word[i:]
            if core.endswith("ay") and len(core) >= 2:
                base = core[:-2]
                out.append(base[::-1] + suffix)
            else:
                out.append(word)
        return " ".join(out)
