class WordBoundaryReversal:
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
                    word = "".join(current)
                    if len(word) >= 4:
                        result.append(word[::-1])
                    else:
                        result.append(word)
                    current = []
                result.append(char)
        if current:
            word = "".join(current)
            if len(word) >= 4:
                result.append(word[::-1])
            else:
                result.append(word)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        current = []
        for char in ciphertext:
            if char.isalpha():
                current.append(char)
            else:
                if current:
                    word = "".join(current)
                    if len(word) >= 4:
                        result.append(word[::-1])
                    else:
                        result.append(word)
                    current = []
                result.append(char)
        if current:
            word = "".join(current)
            if len(word) >= 4:
                result.append(word[::-1])
            else:
                result.append(word)
        return "".join(result)
