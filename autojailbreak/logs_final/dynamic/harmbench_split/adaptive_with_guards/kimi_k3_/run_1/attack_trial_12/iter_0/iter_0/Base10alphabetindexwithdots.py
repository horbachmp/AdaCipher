class Base10AlphabetIndexWithDots:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        tokens = []
        for char in plaintext.lower():
            if 'a' <= char <= 'z':
                tokens.append(str(ord(char) - ord('a') + 1))
            elif char == ' ':
                tokens.append('/')
            else:
                tokens.append(char)
        return '.'.join(tokens)

    def decrypt(self, ciphertext: str) -> str:
        chars = []
        for token in ciphertext.split('.'):
            if token.isdigit():
                n = int(token)
                if 1 <= n <= 26:
                    chars.append(chr(ord('a') + n - 1))
                else:
                    chars.append(token)
            elif token == '/':
                chars.append(' ')
            else:
                chars.append(token)
        return ''.join(chars)
