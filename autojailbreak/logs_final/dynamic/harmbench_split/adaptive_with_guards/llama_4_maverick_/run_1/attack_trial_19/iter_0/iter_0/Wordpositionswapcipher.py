class WordPositionSwapCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        words = plaintext.split(" ")
        swapped = []
        i = 0
        while i < len(words):
            if i + 1 < len(words):
                swapped.append(words[i + 1])
                swapped.append(words[i])
                i += 2
            else:
                swapped.append(words[i])
                i += 1
        return " ".join(swapped)

    def decrypt(self, ciphertext: str) -> str:
        words = ciphertext.split(" ")
        swapped = []
        i = 0
        while i < len(words):
            if i + 1 < len(words):
                swapped.append(words[i + 1])
                swapped.append(words[i])
                i += 2
            else:
                swapped.append(words[i])
                i += 1
        return " ".join(swapped)
