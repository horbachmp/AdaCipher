class VigenereCipherWithFixedKeyKEY:
    def __init__(self):
        self._key_shifts = [10, 4, 24]

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = self._key_shifts[key_index % len(self._key_shifts)]
                if char.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
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
                shift = self._key_shifts[key_index % len(self._key_shifts)]
                if char.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                result.append(chr((ord(char) - base - shift) % 26 + base))
                key_index += 1
            else:
                result.append(char)
        return "".join(result)
