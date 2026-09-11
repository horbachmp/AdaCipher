class VowelConsonantCaseRotator:
    def __init__(self):
        self.vowel_enc = {
            'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
            'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
        }
        self.vowel_dec = {
            'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o', 'a': 'u',
            'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O', 'A': 'U'
        }
        self.consonants = "bcdfghjklmnpqrstvwxyz"
        self.consonant_enc = {}
        self.consonant_dec = {}
        for i, ch in enumerate(self.consonants):
            nxt = self.consonants[(i + 1) % len(self.consonants)]
            prv = self.consonants[(i - 1) % len(self.consonants)]
            self.consonant_enc[ch] = nxt
            self.consonant_enc[ch.upper()] = nxt.upper()
            self.consonant_dec[ch] = prv
            self.consonant_dec[ch.upper()] = prv.upper()

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch in self.vowel_enc:
                out.append(self.vowel_enc[ch])
            elif ch in self.consonant_enc:
                out.append(self.consonant_enc[ch])
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch in self.vowel_dec:
                out.append(self.vowel_dec[ch])
            elif ch in self.consonant_dec:
                out.append(self.consonant_dec[ch])
            else:
                out.append(ch)
        return "".join(out)
