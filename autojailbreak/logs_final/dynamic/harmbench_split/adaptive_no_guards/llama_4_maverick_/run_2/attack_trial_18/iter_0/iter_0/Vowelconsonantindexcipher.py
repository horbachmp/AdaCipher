class VowelConsonantIndexCipher:
    def __init__(self):
        self.vowel_to_digit = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
        self.digit_to_vowel = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
        self.lower_vowels = set('aeiou')
        self.upper_vowels = set('AEIOU')
        self.lower_consonants = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in self.lower_vowels]
        self.upper_consonants = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if c not in self.upper_vowels]
        self.lower_encrypt = {}
        self.upper_encrypt = {}
        self.lower_decrypt = {}
        self.upper_decrypt = {}
        for i, c in enumerate(self.lower_consonants):
            nxt = self.lower_consonants[(i + 1) % len(self.lower_consonants)]
            self.lower_encrypt[c] = nxt
            self.lower_decrypt[nxt] = c
        for i, c in enumerate(self.upper_consonants):
            nxt = self.upper_consonants[(i + 1) % len(self.upper_consonants)]
            self.upper_encrypt[c] = nxt
            self.upper_decrypt[nxt] = c

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch in self.lower_vowels or ch in self.upper_vowels:
                out.append(self.vowel_to_digit[ch.lower()])
            elif ch in self.lower_encrypt:
                out.append(self.lower_encrypt[ch])
            elif ch in self.upper_encrypt:
                out.append(self.upper_encrypt[ch])
            else:
                out.append(ch)
        return ''.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch in self.digit_to_vowel:
                out.append(self.digit_to_vowel[ch])
            elif ch in self.lower_decrypt:
                out.append(self.lower_decrypt[ch])
            elif ch in self.upper_decrypt:
                out.append(self.upper_decrypt[ch])
            else:
                out.append(ch)
        return ''.join(out)
