class VigenereWithFixedKey:
    def __init__(self):
        self.key = "CIPHER"
        self.shifts = [ord(c) - ord('A') for c in self.key]

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        for ch in plaintext:
            if 'A' <= ch <= 'Z':
                shift = self.shifts[key_index % len(self.shifts)]
                result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
                key_index += 1
            elif 'a' <= ch <= 'z':
                shift = self.shifts[key_index % len(self.shifts)]
                result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
                key_index += 1
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        key_index = 0
        for ch in ciphertext:
            if 'A' <= ch <= 'Z':
                shift = self.shifts[key_index % len(self.shifts)]
                result.append(chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A')))
                key_index += 1
            elif 'a' <= ch <= 'z':
                shift = self.shifts[key_index % len(self.shifts)]
                result.append(chr((ord(ch) - ord('a') - shift + 26) % 26 + ord('a')))
                key_index += 1
            else:
                result.append(ch)
        return ''.join(result)
