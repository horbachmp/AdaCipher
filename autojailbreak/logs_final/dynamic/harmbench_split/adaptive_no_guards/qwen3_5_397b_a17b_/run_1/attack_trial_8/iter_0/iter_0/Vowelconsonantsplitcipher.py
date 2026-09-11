class VowelConsonantSplitCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def encrypt(self, plaintext: str) -> str:
        part1 = []
        part2 = []
        for ch in plaintext:
            if ch.isalpha() and ch not in self.vowels:
                part2.append(ch)
            else:
                part1.append(ch)
        return "".join(part1) + "|" + "".join(part2)

    def decrypt(self, ciphertext: str) -> str:
        part1, part2 = ciphertext.split("|", 1)
        consonants = iter(part2)
        result = []
        for ch in part1:
            if ch.isalpha() and ch in self.vowels:
                result.append(ch)
            elif ch.isalpha() and ch not in self.vowels:
                result.append(next(consonants))
            else:
                result.append(ch)
        return "".join(result)
