class Rot13WithUnderscoreSpaceSubstitution:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
            elif 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
            elif ch == ' ':
                result.append('_')
            elif ch == '_':
                result.append(' ')
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
            elif 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
            elif ch == '_':
                result.append(' ')
            elif ch == ' ':
                result.append('_')
            else:
                result.append(ch)
        return ''.join(result)
