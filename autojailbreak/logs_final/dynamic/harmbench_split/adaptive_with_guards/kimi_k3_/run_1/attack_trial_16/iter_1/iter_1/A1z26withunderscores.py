class A1z26WithUnderscores:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        tokens = []
        for ch in plaintext.lower():
            if ch == " ":
                tokens.append("")
            elif "a" <= ch <= "z":
                tokens.append(str(ord(ch) - ord("a") + 1))
            else:
                tokens.append(ch)
        return "_".join(tokens)

    def decrypt(self, ciphertext: str) -> str:
        words = ciphertext.split("__")
        out_words = []
        for word in words:
            chars = []
            if word == "":
                out_words.append("")
                continue
            for token in word.split("_"):
                if token.isdigit():
                    n = int(token)
                    if 1 <= n <= 26:
                        chars.append(chr(ord("a") + n - 1))
                    else:
                        chars.append(token)
                else:
                    chars.append(token)
            out_words.append("".join(chars))
        return " ".join(out_words)
