class ConsonantVowelInterleaveCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for token in plaintext.split(" "):
            if token.isalpha():
                consonants = [ch for ch in token if ch not in self.vowels]
                vowels = [ch for ch in token if ch in self.vowels]
                result.append("".join(consonants + vowels))
            else:
                if any(ch.isalpha() for ch in token):
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
                            elif v_idx < len(vowels):
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
            if token.isalpha():
                c_count = sum(1 for ch in token if ch not in self.vowels)
                consonants = token[:c_count]
                vowels = token[c_count:]
                rebuilt = []
                c_idx = 0
                v_idx = 0
                for i in range(len(token)):
                    if c_idx < len(consonants):
                        rebuilt.append(consonants[c_idx])
                        c_idx += 1
                    elif v_idx < len(vowels):
                        rebuilt.append(vowels[v_idx])
                        v_idx += 1
                result.append("".join(rebuilt))
            else:
                if any(ch.isalpha() for ch in token):
                    alpha_chars = [ch for ch in token if ch.isalpha()]
                    c_count = sum(1 for ch in alpha_chars if ch not in self.vowels)
                    consonants = alpha_chars[:c_count]
                    vowels = alpha_chars[c_count:]
                    rebuilt = []
                    c_idx = 0
                    v_idx = 0
                    for ch in token:
                        if ch.isalpha():
                            if c_idx < len(consonants):
                                rebuilt.append(consonants[c_idx])
                                c_idx += 1
                            elif v_idx < len(vowels):
                                rebuilt.append(vowels[v_idx])
                                v_idx += 1
                        else:
                            rebuilt.append(ch)
                    result.append("".join(rebuilt))
                else:
                    result.append(token)
        return " ".join(result)
