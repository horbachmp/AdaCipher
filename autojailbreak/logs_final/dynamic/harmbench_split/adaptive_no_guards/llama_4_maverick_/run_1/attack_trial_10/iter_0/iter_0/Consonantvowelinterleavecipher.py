class ConsonantVowelInterleaveCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

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
                consonants = "".join(ch for ch in word if ch not in self.vowels)
                vowels = "".join(ch for ch in word if ch in self.vowels)
                if consonants and vowels:
                    result.append(consonants + "-" + vowels)
                else:
                    result.append(word)
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
                while j < n and (ciphertext[j].isalpha() or ciphertext[j] == "-"):
                    j += 1
                token = ciphertext[i:j]
                if "-" in token:
                    consonants, vowels = token.split("-", 1)
                    merged = []
                    c_idx = 0
                    v_idx = 0
                    for ch in token:
                        if ch == "-":
                            continue
                        if c_idx < len(consonants):
                            merged.append(consonants[c_idx])
                            c_idx += 1
                        if v_idx < len(vowels):
                            merged.append(vowels[v_idx])
                            v_idx += 1
                    if c_idx < len(consonants):
                        merged.extend(consonants[c_idx:])
                    if v_idx < len(vowels):
                        merged.extend(vowels[v_idx:])
                    result.append("".join(merged))
                else:
                    result.append(token)
                i = j
            else:
                result.append(ciphertext[i])
                i += 1
        return "".join(result)
