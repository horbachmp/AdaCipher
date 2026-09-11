class VigenereWithFixedKeyKEY:
    def __init__(self):
        self._shifts = (10, 4, 24)

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        for char in plaintext:
            if 'A' <= char <= 'Z':
                shift = self._shifts[key_index]
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
                key_index = (key_index + 1) % 3
            elif 'a' <= char <= 'z':
                shift = self._shifts[key_index]
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
                key_index = (key_index + 1) % 3
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        key_index = 0
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                shift = self._shifts[key_index]
                result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
                key_index = (key_index + 1) % 3
            elif 'a' <= char <= 'z':
                shift = self._shifts[key_index]
                result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
                key_index = (key_index + 1) % 3
            else:
                result.append(char)
        return ''.join(result)
