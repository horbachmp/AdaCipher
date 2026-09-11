class PairwiseCharacterSwap:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        chars = list(plaintext)
        for i in range(0, len(chars) - 1, 2):
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
        return "".join(chars)

    def decrypt(self, ciphertext: str) -> str:
        chars = list(ciphertext)
        for i in range(0, len(chars) - 1, 2):
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
        return "".join(chars)
