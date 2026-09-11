class VowelConsonantShiftTwoCipher:
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    def _transform(self, text: str, shift: int) -> str:
        result = []
        for ch in text:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self.vowels:
                    idx = self.vowels.index(lower)
                    new_ch = self.vowels[(idx + shift) % len(self.vowels)]
                elif lower in self.consonants:
                    idx = self.consonants.index(lower)
                    new_ch = self.consonants[(idx + shift) % len(self.consonants)]
                else:
                    new_ch = lower
                if ch.isupper():
                    new_ch = new_ch.upper()
                result.append(new_ch)
            else:
                result.append(ch)
        return ''.join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext, 2)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext, -2)
