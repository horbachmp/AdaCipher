class A1Z26WithHyphens:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        text = plaintext.lower()
        out = []
        n = len(text)
        for i, ch in enumerate(text):
            if 'a' <= ch <= 'z':
                out.append(str(ord(ch) - ord('a') + 1))
                if i + 1 < n and text[i + 1].isalpha():
                    out.append('-')
            else:
                out.append(ch)
        return ''.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch.isdigit():
                j = i
                while j < n and ciphertext[j].isdigit():
                    j += 1
                num = int(ciphertext[i:j])
                out.append(chr(ord('a') + num - 1))
                if j < n and ciphertext[j] == '-':
                    i = j + 1
                else:
                    i = j
            else:
                out.append(ch)
                i += 1
        return ''.join(out)
