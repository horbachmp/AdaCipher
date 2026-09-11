class MorseCodeWordCipher:
    def __init__(self):
        self._enc = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }
        self._dec = {v: k for k, v in self._enc.items()}

    def encrypt(self, plaintext: str) -> str:
        tokens = []
        for ch in plaintext:
            if ch.isalpha():
                tokens.append(self._enc[ch.lower()])
            elif ch == " ":
                tokens.append("/")
            else:
                tokens.append(ch)
        out = []
        i = 0
        while i < len(tokens):
            tok = tokens[i]
            if tok == "/":
                out.append(" / ")
            else:
                out.append(tok)
                if i + 1 < len(tokens) and tokens[i + 1] != "/":
                    out.append(" ")
            i += 1
        return "".join(out).strip()

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split(" / ")
        words = []
        for part in parts:
            if part == "":
                words.append("")
                continue
            letters = []
            for tok in part.split():
                letters.append(self._dec.get(tok, tok))
            words.append("".join(letters))
        return " ".join(words)
