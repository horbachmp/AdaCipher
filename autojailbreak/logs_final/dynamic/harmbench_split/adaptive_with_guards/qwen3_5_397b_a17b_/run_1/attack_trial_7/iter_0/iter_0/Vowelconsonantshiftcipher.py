class VowelConsonantShiftCipher:
    def __init__(self):
        self.vowels = "aeiou"
        self.vowel_next = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"}
        self.vowel_prev = {"a": "u", "e": "a", "i": "e", "o": "i", "u": "o"}
        consonants = "bcdfghjklmnpqrstvwxyz"
        self.cons_next = {consonants[i]: consonants[(i + 1) % len(consonants)] for i in range(len(consonants))}
        self.cons_prev = {consonants[i]: consonants[(i - 1) % len(consonants)] for i in range(len(consonants))}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            low = ch.lower()
            if low.isalpha():
                if low in self.vowels:
                    mapped = self.vowel_next[low]
                else:
                    mapped = self.cons_next[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            low = ch.lower()
            if low.isalpha():
                if low in self.vowels:
                    mapped = self.vowel_prev[low]
                else:
                    mapped = self.cons_prev[low]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
