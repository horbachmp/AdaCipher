class VigenereCipherWithFixedKeyword:
    def __init__(self):
        self.keyword = "CIPHER"
        self.shifts = [ord(c) - ord('A') for c in self.keyword]

    def encrypt(self, plaintext: str) -> str:
        result = []
        counter = 0
        for char in plaintext:
            if char.isalpha():
                shift = self.shifts[counter % 6]
                base = ord('a') if char.islower() else ord('A')
                result.append(chr((ord(char) - base + shift) % 26 + base))
                counter += 1
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        counter = 0
        for char in ciphertext:
            if char.isalpha():
                shift = self.shifts[counter % 6]
                base = ord('a') if char.islower() else ord('A')
                result.append(chr((ord(char) - base - shift) % 26 + base))
                counter += 1
            else:
                result.append(char)
        return "".join(result)
