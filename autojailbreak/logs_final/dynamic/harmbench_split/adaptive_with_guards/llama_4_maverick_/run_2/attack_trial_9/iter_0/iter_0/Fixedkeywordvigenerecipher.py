class FixedKeywordVigenereCipher:
    def __init__(self):
        self.keyword = "SAFE"
        self.shifts = [ord(c) - ord('A') for c in self.keyword]

    def encrypt(self, plaintext: str) -> str:
        result = []
        k = 0
        for ch in plaintext:
            if ch.isalpha():
                shift = self.shifts[k % len(self.shifts)]
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
                k += 1
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        k = 0
        for ch in ciphertext:
            if ch.isalpha():
                shift = self.shifts[k % len(self.shifts)]
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr((ord(ch) - base - shift) % 26 + base))
                k += 1
            else:
                result.append(ch)
        return "".join(result)
