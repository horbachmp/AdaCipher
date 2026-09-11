class ReverseWordCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        current = []
        for char in plaintext:
            if char.isalpha():
                current.append(char)
            else:
                if current:
                    result.append(''.join(reversed(current)))
                    current = []
                result.append(char)
        if current:
            result.append(''.join(reversed(current)))
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        current = []
        for char in ciphertext:
            if char.isalpha():
                current.append(char)
            else:
                if current:
                    result.append(''.join(reversed(current)))
                    current = []
                result.append(char)
        if current:
            result.append(''.join(reversed(current)))
        return ''.join(result)
