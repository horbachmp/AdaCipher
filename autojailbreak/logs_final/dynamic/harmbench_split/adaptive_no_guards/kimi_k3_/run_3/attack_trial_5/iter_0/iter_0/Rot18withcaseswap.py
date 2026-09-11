class Rot18WithCaseSwap:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if 'A' <= ch <= 'Z':
                shifted = chr((ord(ch) - ord('A') + 13) % 26 + ord('a'))
                result.append(shifted)
            elif 'a' <= ch <= 'z':
                shifted = chr((ord(ch) - ord('a') + 13) % 26 + ord('A'))
                result.append(shifted)
            elif '0' <= ch <= '9':
                result.append(str((ord(ch) - ord('0') + 5) % 10))
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if 'A' <= ch <= 'Z':
                shifted = chr((ord(ch) - ord('A') - 13) % 26 + ord('a'))
                result.append(shifted)
            elif 'a' <= ch <= 'z':
                shifted = chr((ord(ch) - ord('a') - 13) % 26 + ord('A'))
                result.append(shifted)
            elif '0' <= ch <= '9':
                result.append(str((ord(ch) - ord('0') - 5) % 10))
            else:
                result.append(ch)
        return ''.join(result)
