class ReverseAlphabetWithShiftThree:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if 'a' <= ch <= 'z':
                x = ord(ch) - ord('a')
                mapped = ((25 - x) + 3) % 26
                result.append(chr(mapped + ord('a')))
            elif 'A' <= ch <= 'Z':
                x = ord(ch) - ord('A')
                mapped = ((25 - x) + 3) % 26
                result.append(chr(mapped + ord('A')))
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if 'a' <= ch <= 'z':
                y = ord(ch) - ord('a')
                mapped = 25 - ((y - 3) % 26)
                result.append(chr(mapped + ord('a')))
            elif 'A' <= ch <= 'Z':
                y = ord(ch) - ord('A')
                mapped = 25 - ((y - 3) % 26)
                result.append(chr(mapped + ord('A')))
            else:
                result.append(ch)
        return ''.join(result)
