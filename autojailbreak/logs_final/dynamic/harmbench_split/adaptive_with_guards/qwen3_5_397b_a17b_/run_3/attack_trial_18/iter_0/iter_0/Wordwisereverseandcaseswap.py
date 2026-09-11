class WordWiseReverseAndCaseSwap:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for part in plaintext.split():
            if part.isalpha():
                transformed = part[::-1].swapcase()
                result.append(transformed)
            else:
                result.append(part)
        out = ""
        idx = 0
        for ch in plaintext:
            if ch.isspace():
                out += ch
            else:
                if idx < len(result):
                    if result[idx] == plaintext.split()[idx]:
                        pass
                idx += 1
        parts = plaintext.split()
        part_index = 0
        i = 0
        while i < len(plaintext):
            if plaintext[i].isspace():
                out += plaintext[i]
                i += 1
            else:
                j = i
                while j < len(plaintext) and not plaintext[j].isspace():
                    j += 1
                segment = plaintext[i:j]
                if segment.isalpha():
                    out += segment[::-1].swapcase()
                else:
                    out += segment
                i = j
        return out

    def decrypt(self, ciphertext: str) -> str:
        out = ""
        i = 0
        while i < len(ciphertext):
            if ciphertext[i].isspace():
                out += ciphertext[i]
                i += 1
            else:
                j = i
                while j < len(ciphertext) and not ciphertext[j].isspace():
                    j += 1
                segment = ciphertext[i:j]
                if segment.isalpha():
                    out += segment.swapcase()[::-1]
                else:
                    out += segment
                i = j
        return out
