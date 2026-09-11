class VowelConsonantSplitReversalCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for token in plaintext.split(" "):
            if token and any(ch.isalpha() for ch in token):
                consonants = [ch for ch in token if ch.isalpha() and ch not in self.vowels]
                vowels = [ch for ch in token if ch.isalpha() and ch in self.vowels]
                rebuilt = []
                c_idx = 0
                v_idx = 0
                for ch in token:
                    if ch.isalpha():
                        if c_idx < len(consonants):
                            rebuilt.append(consonants[c_idx])
                            c_idx += 1
                        else:
                            rebuilt.append(vowels[v_idx])
                            v_idx += 1
                    else:
                        rebuilt.append(ch)
                result.append("".join(rebuilt))
            else:
                result.append(token)
        return " ".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for token in ciphertext.split(" "):
            if token and any(ch.isalpha() for ch in token):
                letters = [ch for ch in token if ch.isalpha()]
                n = len(letters)
                split = 0
                for i in range(n + 1):
                    consonants = letters[:i]
                    vowels = letters[i:]
                    if len(consonants) >= len(vowels) or i == n:
                        split = i
                        break
                consonants = letters[:split]
                vowels = letters[split:]
                c_idx = 0
                v_idx = 0
                rebuilt = []
                for ch in token:
                    if ch.isalpha():
                        if c_idx < len(consonants):
                            rebuilt.append(consonants[c_idx])
                            c_idx += 1
                        else:
                            rebuilt.append(vowels[v_idx])
                            v_idx += 1
                    else:
                        rebuilt.append(ch)
                result.append("".join(rebuilt))
            else:
                result.append(token)
        return " ".join(result)
