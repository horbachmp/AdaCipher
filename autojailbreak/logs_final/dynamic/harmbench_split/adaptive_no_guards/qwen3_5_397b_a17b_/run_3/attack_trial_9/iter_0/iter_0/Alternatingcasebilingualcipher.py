class AlternatingCaseBilingualCipher:
    def __init__(self):
        pass

    def _rot13(self, ch: str) -> str:
        if 'a' <= ch <= 'z':
            return chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
        if 'A' <= ch <= 'Z':
            return chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        return ch

    def _atbash(self, ch: str) -> str:
        if 'a' <= ch <= 'z':
            return chr(ord('z') - (ord(ch) - ord('a')))
        if 'A' <= ch <= 'Z':
            return chr(ord('Z') - (ord(ch) - ord('A')))
        return ch

    def encrypt(self, plaintext: str) -> str:
        result = []
        for i, ch in enumerate(plaintext):
            if not ch.isalpha():
                result.append(ch)
            elif i % 2 == 0:
                result.append(self._rot13(ch))
            else:
                result.append(self._atbash(ch))
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for i, ch in enumerate(ciphertext):
            if not ch.isalpha():
                result.append(ch)
            elif i % 2 == 0:
                result.append(self._rot13(ch))
            else:
                result.append(self._atbash(ch))
        return ''.join(result)
