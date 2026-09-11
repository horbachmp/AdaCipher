class VigenereCipherWithFixedKey:
    def __init__(self):
        self.key = "CIPHER"
        self.key_shifts = [ord(c) - ord('A') for c in self.key]

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = self.key_shifts[key_index % len(self.key_shifts)]
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base + shift) % 26 + base))
                key_index += 1
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = self.key_shifts[key_index % len(self.key_shifts)]
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base - shift) % 26 + base))
                key_index += 1
            else:
                result.append(char)
        return "".join(result)
