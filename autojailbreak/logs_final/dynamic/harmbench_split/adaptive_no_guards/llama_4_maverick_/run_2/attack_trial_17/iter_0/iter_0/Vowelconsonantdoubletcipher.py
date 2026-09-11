class VowelConsonantDoubletCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        vowels = set("aeiouAEIOU")
        result = []
        for ch in plaintext:
            if ch in vowels:
                result.append(ch * 2)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        vowels = set("aeiouAEIOU")
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if i + 1 < n and ch == ciphertext[i + 1] and ch in vowels:
                result.append(ch)
                i += 2
            else:
                result.append(ch)
                i += 1
        return "".join(result)
