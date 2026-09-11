class Rot13WithVowelUnderscore:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if 'A' <= ch <= 'Z':
                enc = chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
                result.append('_' if enc in 'AEIOU' else enc)
            elif 'a' <= ch <= 'z':
                enc = chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
                result.append('_' if enc in 'aeiou' else enc)
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch == '_':
                result.append('_')
            elif 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
            elif 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
            else:
                result.append(ch)
        return ''.join(result)
