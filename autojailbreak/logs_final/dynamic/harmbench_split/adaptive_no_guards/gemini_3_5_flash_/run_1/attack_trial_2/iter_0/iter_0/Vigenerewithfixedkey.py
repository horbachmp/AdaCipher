class VigenereWithFixedKey:
    def __init__(self):
        self._shifts = [10, 4, 24]

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = self._shifts[key_index % 3]
                if char.isupper():
                    base = 65
                else:
                    base = 97
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
                shift = self._shifts[key_index % 3]
                if char.isupper():
                    base = 65
                else:
                    base = 97
                result.append(chr((ord(char) - base - shift) % 26 + base))
                key_index += 1
            else:
                result.append(char)
        return "".join(result)
