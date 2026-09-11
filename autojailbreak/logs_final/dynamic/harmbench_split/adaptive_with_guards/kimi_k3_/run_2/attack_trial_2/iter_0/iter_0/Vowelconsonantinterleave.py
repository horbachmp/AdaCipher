class VowelConsonantInterleave:
    def __init__(self):
        self.vowels = set("aeiouyAEIOUY")

    def encrypt(self, plaintext: str) -> str:
        vowels = []
        rest = []
        for ch in plaintext:
            if ch in self.vowels:
                vowels.append(ch)
                rest.append('_')
            else:
                rest.append(ch)
        return "".join(vowels) + "|" + "".join(rest)

    def decrypt(self, ciphertext: str) -> str:
        if "|" not in ciphertext:
            return ciphertext
        vowels_part, rest_part = ciphertext.split("|", 1)
        vowels_iter = iter(vowels_part)
        result = []
        for ch in rest_part:
            if ch == '_':
                result.append(next(vowels_iter, '_'))
            else:
                result.append(ch)
        return "".join(result)
