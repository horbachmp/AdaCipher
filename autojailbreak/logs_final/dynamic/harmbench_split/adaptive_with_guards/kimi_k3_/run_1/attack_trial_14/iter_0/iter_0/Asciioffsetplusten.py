class AsciiOffsetPlusTen:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            code = ord(ch)
            if 32 <= code <= 126:
                new_code = 32 + ((code - 32 + 10) % 95)
                result.append(chr(new_code))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            code = ord(ch)
            if 32 <= code <= 126:
                original_code = 32 + ((code - 32 - 10) % 95)
                result.append(chr(original_code))
            else:
                result.append(ch)
        return "".join(result)
