class Base6AlphabetShift:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                pos = ord(ch.upper()) - ord('A')
                code = format(pos // 6, 'd') + format(pos % 6, 'd')
                result.append(code)
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            c1 = ciphertext[i]
            if i + 1 < n and c1.isdigit() and ciphertext[i + 1].isdigit():
                d1 = ord(c1) - ord('0')
                d2 = ord(ciphertext[i + 1]) - ord('0')
                if 0 <= d1 <= 5 and 0 <= d2 <= 5:
                    val = d1 * 6 + d2
                    if 0 <= val < 26:
                        result.append(chr(ord('A') + val))
                        i += 2
                        continue
            result.append(c1)
            i += 1
        return ''.join(result)
