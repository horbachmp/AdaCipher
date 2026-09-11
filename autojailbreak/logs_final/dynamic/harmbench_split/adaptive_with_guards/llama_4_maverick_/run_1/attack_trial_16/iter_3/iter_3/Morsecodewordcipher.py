class MorseCodeWordCipher:
    def __init__(self):
        self._encode = {
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
        self._decode = {v: k for k, v in self._encode.items()}

    def encrypt(self, plaintext: str) -> str:
        tokens = []
        current = []
        for ch in plaintext:
            if ch.isalpha():
                current.append(self._encode[ch.lower()])
            else:
                if current:
                    tokens.append(" ".join(current))
                    current = []
                tokens.append(ch)
        if current:
            tokens.append(" ".join(current))
        return " / ".join(tokens)

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split(" / ")
        out = []
        for part in parts:
            if not part:
                continue
            if all(ch in ".- " for ch in part):
                letters = []
                for seq in part.split():
                    letters.append(self._decode.get(seq, seq))
                out.append("".join(letters))
            else:
                out.append(part)
        return " ".join(out)
