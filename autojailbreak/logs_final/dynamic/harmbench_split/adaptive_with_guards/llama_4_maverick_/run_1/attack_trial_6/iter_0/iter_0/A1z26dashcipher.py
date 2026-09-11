class A1Z26DashCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        words = plaintext.lower().split(" ")
        encoded_words = []
        for word in words:
            tokens = []
            for ch in word:
                if "a" <= ch <= "z":
                    tokens.append(str(ord(ch) - ord("a") + 1))
                else:
                    tokens.append(ch)
            encoded_words.append("-".join(tokens))
        return " ".join(encoded_words)

    def decrypt(self, ciphertext: str) -> str:
        words = ciphertext.split(" ")
        decoded_words = []
        for word in words:
            if word == "":
                decoded_words.append("")
                continue
            tokens = word.split("-")
            chars = []
            for token in tokens:
                if token.isdigit():
                    n = int(token)
                    if 1 <= n <= 26:
                        chars.append(chr(ord("a") + n - 1))
                    else:
                        chars.append(token)
                else:
                    chars.append(token)
            decoded_words.append("".join(chars))
        return " ".join(decoded_words)
