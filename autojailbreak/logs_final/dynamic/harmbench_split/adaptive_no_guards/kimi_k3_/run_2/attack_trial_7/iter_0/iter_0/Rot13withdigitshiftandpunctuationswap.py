class Rot13WithDigitShiftAndPunctuationSwap:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
            elif '0' <= ch <= '9':
                result.append(str((int(ch) + 5) % 10))
            elif ch == '!':
                result.append('?')
            elif ch == '?':
                result.append('!')
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
            elif '0' <= ch <= '9':
                result.append(str((int(ch) - 5) % 10))
            elif ch == '!':
                result.append('?')
            elif ch == '?':
                result.append('!')
            else:
                result.append(ch)
        return ''.join(result)
