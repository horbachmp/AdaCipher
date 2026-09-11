class WordwiseReverseWithMarker:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        i = 0
        n = len(plaintext)
        while i < n:
            if plaintext[i].isalpha():
                j = i
                while j < n and plaintext[j].isalpha():
                    j += 1
                word = plaintext[i:j]
                result.append(word[::-1] + "*")
                i = j
            else:
                result.append(plaintext[i])
                i += 1
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            if ciphertext[i].isalpha():
                j = i
                while j < n and ciphertext[j].isalpha():
                    j += 1
                if j < n and ciphertext[j] == "*":
                    result.append(ciphertext[i:j][::-1])
                    i = j + 1
                else:
                    result.append(ciphertext[i:j])
                    i = j
            else:
                result.append(ciphertext[i])
                i += 1
        return "".join(result)
