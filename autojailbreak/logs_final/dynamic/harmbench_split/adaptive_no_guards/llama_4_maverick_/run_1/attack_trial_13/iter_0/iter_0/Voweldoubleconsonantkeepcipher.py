class VowelDoubleConsonantKeepCipher:
    def __init__(self):
        self._vowels = set("aeiouAEIOU")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._vowels:
                result.append(ch * 2)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch in self._vowels and i + 1 < n and ciphertext[i + 1] == ch:
                result.append(ch)
                i += 2
            else:
                result.append(ch)
                i += 1
        return "".join(result)
