class AsciiOffsetCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            o = ord(ch)
            if 32 <= o <= 124:
                result.append(chr(o + 2))
            elif o == 125 or o == 126:
                result.append(chr(o - 93))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            o = ord(ch)
            if 34 <= o <= 126:
                result.append(chr(o - 2))
            elif o == 32 or o == 33:
                result.append(chr(o + 93))
            else:
                result.append(ch)
        return "".join(result)
