class Base10AsciiShiftCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        words = plaintext.split(" ")
        enc_words = []
        for word in words:
            if word == "":
                enc_words.append("")
            else:
                enc_words.append("-".join(str(ord(ch) + 10) for ch in word))
        return " ".join(enc_words)

    def decrypt(self, ciphertext: str) -> str:
        words = ciphertext.split(" ")
        dec_words = []
        for word in words:
            if word == "":
                dec_words.append("")
            else:
                chars = []
                for part in word.split("-"):
                    if part == "":
                        continue
                    chars.append(chr(int(part) - 10))
                dec_words.append("".join(chars))
        return " ".join(dec_words)
