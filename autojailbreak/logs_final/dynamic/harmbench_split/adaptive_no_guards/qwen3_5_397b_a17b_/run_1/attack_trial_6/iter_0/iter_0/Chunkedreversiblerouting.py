class ChunkedReversibleRouting:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        chunks = []
        for i in range(0, len(plaintext), 3):
            block = plaintext[i:i + 3]
            chunks.append(block[::-1] if len(block) == 3 else block)
        return "".join(chunks)

    def decrypt(self, ciphertext: str) -> str:
        chunks = []
        for i in range(0, len(ciphertext), 3):
            block = ciphertext[i:i + 3]
            chunks.append(block[::-1] if len(block) == 3 else block)
        return "".join(chunks)
