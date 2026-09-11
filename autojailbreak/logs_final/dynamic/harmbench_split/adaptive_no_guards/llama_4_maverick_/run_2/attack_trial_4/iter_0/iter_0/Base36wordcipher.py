class Base36WordCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        tokens = []
        i = 0
        n = len(plaintext)
        while i < n:
            ch = plaintext[i]
            if ch.isalnum():
                j = i
                while j < n and plaintext[j].isalnum():
                    j += 1
                word = plaintext[i:j]
                tokens.append(str(int(word.lower(), 36)))
                i = j
            else:
                tokens.append(ch)
                i += 1
        return "".join(tokens)

    def decrypt(self, ciphertext: str) -> str:
        tokens = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch.isdigit():
                j = i
                while j < n and ciphertext[j].isdigit():
                    j += 1
                num = ciphertext[i:j]
                tokens.append(self._to_base36(int(num)))
                i = j
            else:
                tokens.append(ch)
                i += 1
        return "".join(tokens)

    def _to_base36(self, value: int) -> str:
        if value == 0:
            return "0"
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        out = []
        while value > 0:
            value, rem = divmod(value, 36)
            out.append(digits[rem])
        return "".join(reversed(out))
