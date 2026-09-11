class A1Z26WithHyphens:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        out = []
        n = len(plaintext)
        for i, ch in enumerate(plaintext):
            if ch.isalpha():
                out.append(str(ord(ch.lower()) - ord('a') + 1))
                if i + 1 < n and plaintext[i + 1].isalpha():
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
                while j < n and (ciphertext[j].isdigit() or ciphertext[j] == '-'):
                    j += 1
                segment = ciphertext[i:j]
                parts = segment.split('-')
                for part in parts:
                    if part:
                        out.append(chr(int(part) - 1 + ord('a')))
                i = j
            else:
                out.append(ch)
                i += 1
        return ''.join(out)
