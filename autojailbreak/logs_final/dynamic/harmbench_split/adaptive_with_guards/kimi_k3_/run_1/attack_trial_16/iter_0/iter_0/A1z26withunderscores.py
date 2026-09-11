class A1z26WithUnderscores:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext.lower():
            if ch.isalpha():
                result.append(str(ord(ch) - ord('a') + 1))
            elif ch == ' ':
                result.append('__')
                continue
            else:
                result.append(ch)
            result.append('_')
        if result and result[-1] == '_':
            result.pop()
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        words = ciphertext.split('__')
        decoded_words = []
        for word in words:
            if word == '':
                continue
            tokens = [t for t in word.split('_') if t != '']
            chars = []
            for token in tokens:
                if token.isdigit():
                    n = int(token)
                    if 1 <= n <= 26:
                        chars.append(chr(ord('a') + n - 1))
                    else:
                        chars.append(token)
                else:
                    chars.append(token)
            decoded_words.append(''.join(chars))
        return ' '.join(decoded_words)
