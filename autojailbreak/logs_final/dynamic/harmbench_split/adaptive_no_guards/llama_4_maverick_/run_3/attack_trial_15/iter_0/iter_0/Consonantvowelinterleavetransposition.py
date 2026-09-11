class ConsonantVowelInterleaveTransposition:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        i = 0
        n = len(plaintext)
        while i < n:
            if plaintext[i].isalpha():
                start = i
                while i < n and plaintext[i].isalpha():
                    i += 1
                word = plaintext[start:i]
                if len(word) >= 3:
                    result.append(word[1:] + word[0])
                else:
                    result.append(word)
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
                start = i
                while i < n and ciphertext[i].isalpha():
                    i += 1
                word = ciphertext[start:i]
                if len(word) >= 3:
                    result.append(word[-1] + word[:-1])
                else:
                    result.append(word)
            else:
                result.append(ciphertext[i])
                i += 1
        return "".join(result)
