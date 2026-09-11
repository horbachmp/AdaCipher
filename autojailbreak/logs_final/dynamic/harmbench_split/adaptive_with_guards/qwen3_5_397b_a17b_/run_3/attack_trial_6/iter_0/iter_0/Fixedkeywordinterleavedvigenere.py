class FixedKeywordInterleavedVigenere:
    def __init__(self):
        self.shifts = [18, 0, 5, 4]

    def encrypt(self, plaintext: str) -> str:
        result = []
        letter_position = 0
        for char in plaintext:
            if char.isalpha():
                shift = self.shifts[letter_position % 4]
                base = ord('a') if char.islower() else ord('A')
                result.append(chr((ord(char) - base + shift) % 26 + base))
                letter_position += 1
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        letter_position = 0
        for char in ciphertext:
            if char.isalpha():
                shift = self.shifts[letter_position % 4]
                base = ord('a') if char.islower() else ord('A')
                result.append(chr((ord(char) - base - shift) % 26 + base))
                letter_position += 1
            else:
                result.append(char)
        return "".join(result)
