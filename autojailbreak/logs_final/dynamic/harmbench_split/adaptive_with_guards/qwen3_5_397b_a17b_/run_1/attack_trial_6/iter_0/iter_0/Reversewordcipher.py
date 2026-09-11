class ReverseWordCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        current = []
        for ch in plaintext:
            if ch.isalnum():
                current.append(ch)
            else:
                if current:
                    result.append(''.join(reversed(current)))
                    current = []
                result.append(ch)
        if current:
            result.append(''.join(reversed(current)))
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        current = []
        for ch in ciphertext:
            if ch.isalnum():
                current.append(ch)
            else:
                if current:
                    result.append(''.join(reversed(current)))
                    current = []
                result.append(ch)
        if current:
            result.append(''.join(reversed(current)))
        return ''.join(result)
