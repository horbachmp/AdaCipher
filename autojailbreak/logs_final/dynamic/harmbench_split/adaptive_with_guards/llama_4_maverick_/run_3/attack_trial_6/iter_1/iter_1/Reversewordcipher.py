class ReverseWordCipher:
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
                    result.append(''.join(reversed(word)))
                    word = []
                result.append(ch)
        if word:
            result.append(''.join(reversed(word)))
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        word = []
        for ch in ciphertext:
            if ch.isalpha():
                word.append(ch)
            else:
                if word:
                    result.append(''.join(reversed(word)))
                    word = []
                result.append(ch)
        if word:
            result.append(''.join(reversed(word)))
        return ''.join(result)
