class VowelConsonantSplitCipher:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

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
                consonants = [ch for ch in word if ch not in self.vowels]
                vowels = [ch for ch in word if ch in self.vowels]
                result.append("".join(consonants + vowels))
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
                word = ciphertext[i:j]
                consonants = [ch for ch in word if ch not in self.vowels]
                vowels = [ch for ch in word if ch in self.vowels]
                c_idx = 0
                v_idx = 0
                original = []
                for ch in word:
                    if ch in self.vowels:
                        if v_idx < len(vowels):
                            original.append(vowels[v_idx])
                            v_idx += 1
                    else:
                        if c_idx < len(consonants):
                            original.append(consonants[c_idx])
                            c_idx += 1
                result.append("".join(original))
                i = j
            else:
                result.append(ciphertext[i])
                i += 1
        return "".join(result)
