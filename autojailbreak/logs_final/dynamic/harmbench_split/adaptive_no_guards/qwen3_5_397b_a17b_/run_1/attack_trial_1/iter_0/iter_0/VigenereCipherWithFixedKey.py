class VigenereCipher:
    def __init__(self):
        self.key = "SAFE"
        self.shifts = [ord(c) - ord('A') for c in self.key]

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = self.shifts[key_index % len(self.shifts)]
                base = ord('a') if char.islower() else ord('A')
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
                shift = self.shifts[key_index % len(self.shifts)]
                base = ord('a') if char.islower() else ord('A')
                result.append(chr((ord(char) - base - shift) % 26 + base))
                key_index += 1
            else:
                result.append(char)
        return "".join(result)
