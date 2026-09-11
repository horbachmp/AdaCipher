class VigenereWithFixedKey:
    def __init__(self):
        self._shifts = [10, 4, 24]

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        for ch in plaintext:
            if ch.isalpha():
                shift = self._shifts[key_index % 3]
                base = ord('a') if ch.islower() else ord('A')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
                key_index += 1
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        key_index = 0
        for ch in ciphertext:
            if ch.isalpha():
                shift = self._shifts[key_index % 3]
                base = ord('a') if ch.islower() else ord('A')
                result.append(chr((ord(ch) - base - shift) % 26 + base))
                key_index += 1
            else:
                result.append(ch)
        return "".join(result)
