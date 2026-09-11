class VowelConsonantInterleaveTransposition:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        word = []
        for ch in plaintext:
            if ch.isalpha():
                word.append(ch)
            else:
                if word:
                    if len(word) >= 3:
                        result.append("".join(word[1:]) + word[0])
                    else:
                        result.append("".join(word))
                    word = []
                result.append(ch)
        if word:
            if len(word) >= 3:
                result.append("".join(word[1:]) + word[0])
            else:
                result.append("".join(word))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        word = []
        for ch in ciphertext:
            if ch.isalpha():
                word.append(ch)
            else:
                if word:
                    if len(word) >= 3:
                        result.append(word[-1] + "".join(word[:-1]))
                    else:
                        result.append("".join(word))
                    word = []
                result.append(ch)
        if word:
            if len(word) >= 3:
                result.append(word[-1] + "".join(word[:-1]))
            else:
                result.append("".join(word))
        return "".join(result)
