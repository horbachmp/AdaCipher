class ReverseWordCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        tokens = plaintext.split()
        result = []
        for token in tokens:
            if token.isalpha():
                result.append(token[::-1])
            else:
                result.append(token)
        return " ".join(result)

    def decrypt(self, ciphertext: str) -> str:
        tokens = ciphertext.split()
        result = []
        for token in tokens:
            if token.isalpha():
                result.append(token[::-1])
            else:
                result.append(token)
        return " ".join(result)
