class AlternatingCaseAndReverseCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        reversed_text = plaintext[::-1]
        result = []
        for char in reversed_text:
            if 'A' <= char <= 'Z':
                result.append(char.lower())
            elif 'a' <= char <= 'z':
                result.append(char.upper())
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        swapped = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                swapped.append(char.lower())
            elif 'a' <= char <= 'z':
                swapped.append(char.upper())
            else:
                swapped.append(char)
        return ''.join(swapped)[::-1]
