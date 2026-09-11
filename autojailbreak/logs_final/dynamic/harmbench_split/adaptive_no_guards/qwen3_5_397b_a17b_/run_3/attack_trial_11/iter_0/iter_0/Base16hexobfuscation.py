class Base16HexObfuscation:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch == " " or ch == "\n":
                result.append(ch)
            else:
                result.append(format(ord(ch), "02x"))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split(" ")
        decoded_parts = []
        for part in parts:
            if part == "\n":
                decoded_parts.append(part)
                continue
            if part == "":
                decoded_parts.append("")
                continue
            chars = []
            for i in range(0, len(part), 2):
                pair = part[i:i + 2]
                if len(pair) == 2:
                    chars.append(chr(int(pair, 16)))
            decoded_parts.append("".join(chars))
        return " ".join(decoded_parts)
