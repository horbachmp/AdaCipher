class Base36CharacterEncoding:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        def to_base36(n: int) -> str:
            if n == 0:
                return "0"
            digits = "0123456789abcdefghijklmnopqrstuvwxyz"
            out = []
            while n > 0:
                n, r = divmod(n, 36)
                out.append(digits[r])
            return "".join(reversed(out))

        return "/".join(to_base36(ord(ch)) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        if ciphertext == "":
            return ""
        return "".join(chr(int(part, 36)) for part in ciphertext.split("/"))
