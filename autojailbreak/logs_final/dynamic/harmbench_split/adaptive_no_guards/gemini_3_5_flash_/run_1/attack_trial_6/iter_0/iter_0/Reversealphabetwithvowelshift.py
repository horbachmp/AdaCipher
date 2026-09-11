class ReverseAlphabetWithVowelShift:
    def __init__(self):
        self.vowels = "AEIOU"
        self.vowel_next = {self.vowels[i]: self.vowels[(i + 1) % 5] for i in range(5)}
        self.vowel_prev = {self.vowels[i]: self.vowels[(i - 1) % 5] for i in range(5)}
        self.atbash = {}
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        reversed_alphabet = alphabet[::-1]
        for a, b in zip(alphabet, reversed_alphabet):
            self.atbash[a] = b
            self.atbash[b] = a

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                upper = ch.upper()
                if upper in self.vowel_next:
                    mapped = self.vowel_next[upper]
                else:
                    mapped = self.atbash[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                upper = ch.upper()
                if upper in self.vowel_prev:
                    mapped = self.vowel_prev[upper]
                else:
                    mapped = self.atbash[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)
