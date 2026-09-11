class ChunkedReversibleRouting:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for i in range(0, len(plaintext), 3):
            chunk = plaintext[i:i + 3]
            if len(chunk) == 3:
                result.append(chunk[1] + chunk[2] + chunk[0])
            else:
                result.append(chunk)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for i in range(0, len(ciphertext), 3):
            chunk = ciphertext[i:i + 3]
            if len(chunk) == 3:
                result.append(chunk[2] + chunk[0] + chunk[1])
            else:
                result.append(chunk)
        return "".join(result)
