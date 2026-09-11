class Base36AlphabetShift:
    def __init__(self):
        self.alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.shift = 3
        self.index = {ch: i for i, ch in enumerate(self.alphabet)}

    def encrypt(self, plaintext: str) -> str:
        text = plaintext.upper()
        out = []
        for ch in text:
            if ch in self.index:
                out.append(self.alphabet[(self.index[ch] + self.shift) % 36])
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch in self.index:
                out.append(self.alphabet[(self.index[ch] - self.shift) % 36])
            else:
                out.append(ch)
        return "".join(out)
