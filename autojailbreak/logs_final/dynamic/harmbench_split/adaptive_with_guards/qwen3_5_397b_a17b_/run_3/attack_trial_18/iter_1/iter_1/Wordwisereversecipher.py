class WordWiseReverseCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        i = 0
        n = len(plaintext)
        while i < n:
            ch = plaintext[i]
            if ch.isalpha():
                j = i
                while j < n and plaintext[j].isalpha():
                    j += 1
                result.append(plaintext[i:j][::-1])
                i = j
            else:
                result.append(ch)
                i += 1
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch.isalpha():
                j = i
                while j < n and ciphertext[j].isalpha():
                    j += 1
                result.append(ciphertext[i:j][::-1])
                i = j
            else:
                result.append(ch)
                i += 1
        return "".join(result)
