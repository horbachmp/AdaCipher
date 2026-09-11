class A1z26WithSpaces:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        tokens = []
        for ch in plaintext:
            if ch.isalpha():
                tokens.append(str(ord(ch.lower()) - ord('a') + 1))
            elif ch == ' ':
                tokens.append('/')
            else:
                tokens.append(ch)
        return ' '.join(tokens)

    def decrypt(self, ciphertext: str) -> str:
        tokens = ciphertext.split()
        out = []
        for tok in tokens:
            if tok == '/':
                out.append(' ')
            elif tok.isdigit():
                n = int(tok)
                if 1 <= n <= 26:
                    out.append(chr(ord('a') + n - 1))
                else:
                    out.append(tok)
            else:
                out.append(tok)
        return ''.join(out)
