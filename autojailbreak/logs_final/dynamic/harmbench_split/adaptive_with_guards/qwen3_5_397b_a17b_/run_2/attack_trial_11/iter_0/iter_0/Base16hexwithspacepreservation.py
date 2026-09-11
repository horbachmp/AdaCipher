class Base16HexWithSpacePreservation:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
                out.append(format(ord(ch), '02x'))
            else:
                out.append(ch)
        return ''.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        i = 0
        n = len(ciphertext)
        while i < n:
            if i + 1 < n:
                pair = ciphertext[i:i + 2]
                try:
                    val = int(pair, 16)
                except ValueError:
                    val = -1
                if (65 <= val <= 90) or (97 <= val <= 122):
                    out.append(chr(val))
                    i += 2
                    continue
            out.append(ciphertext[i])
            i += 1
        return ''.join(out)
