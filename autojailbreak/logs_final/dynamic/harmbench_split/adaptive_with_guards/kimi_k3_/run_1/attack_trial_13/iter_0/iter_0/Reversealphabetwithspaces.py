class ReverseAlphabetWithSpaces:
    def __init__(self):
        pass

    def _atbash(self, text: str) -> str:
        result = []
        for ch in text:
            if 'a' <= ch <= 'z':
                result.append(chr(ord('z') - (ord(ch) - ord('a'))))
            elif 'A' <= ch <= 'Z':
                result.append(chr(ord('Z') - (ord(ch) - ord('A'))))
            else:
                result.append(ch)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        transformed = []
        for ch in plaintext:
            if ch == '':
                continue
            if ch == ' ':
                transformed.append('/')
            else:
                transformed.append(self._atbash(ch))
        return ' '.join(transformed)

    def decrypt(self, ciphertext: str) -> str:
        joined = ciphertext.replace(' ', '')
        joined = joined.replace('/', ' ')
        return self._atbash(joined)
