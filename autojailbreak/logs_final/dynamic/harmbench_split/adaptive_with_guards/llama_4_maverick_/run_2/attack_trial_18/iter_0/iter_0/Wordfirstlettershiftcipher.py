class WordFirstLetterShiftCipher:
    def __init__(self):
        pass

    def _shift_char(self, ch: str, n: int) -> str:
        if 'a' <= ch <= 'z':
            return chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        if 'A' <= ch <= 'Z':
            return chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        return ch

    def encrypt(self, plaintext: str) -> str:
        result = []
        i = 0
        length = len(plaintext)
        while i < length:
            ch = plaintext[i]
            if ch.isalpha():
                result.append(self._shift_char(ch, 1))
                i += 1
                while i < length and plaintext[i].isalpha():
                    result.append(plaintext[i])
                    i += 1
            else:
                result.append(ch)
                i += 1
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        length = len(ciphertext)
        while i < length:
            ch = ciphertext[i]
            if ch.isalpha():
                result.append(self._shift_char(ch, -1))
                i += 1
                while i < length and ciphertext[i].isalpha():
                    result.append(ciphertext[i])
                    i += 1
            else:
                result.append(ch)
                i += 1
        return ''.join(result)
