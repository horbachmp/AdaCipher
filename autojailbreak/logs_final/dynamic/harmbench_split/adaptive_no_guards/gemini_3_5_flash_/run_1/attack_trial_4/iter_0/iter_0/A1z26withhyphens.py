class A1Z26WithHyphens:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        tokens = []
        current = []
        for ch in plaintext:
            if ch.isalpha():
                current.append(str(ord(ch.lower()) - ord('a') + 1))
            else:
                if current:
                    tokens.append("-".join(current))
                    current = []
                tokens.append(ch)
        if current:
            tokens.append("-".join(current))
        return " ".join(tokens)

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split(" ")
        result = []
        for part in parts:
            if part == "":
                continue
            if all(piece.isdigit() for piece in part.split("-")) and "-" in part or part.isdigit():
                letters = []
                valid = True
                for piece in part.split("-"):
                    if not piece.isdigit():
                        valid = False
                        break
                    n = int(piece)
                    if not 1 <= n <= 26:
                        valid = False
                        break
                    letters.append(chr(ord('a') + n - 1))
                if valid:
                    result.append("".join(letters))
                else:
                    result.append(part)
            else:
                result.append(part)
        return " ".join(result)
