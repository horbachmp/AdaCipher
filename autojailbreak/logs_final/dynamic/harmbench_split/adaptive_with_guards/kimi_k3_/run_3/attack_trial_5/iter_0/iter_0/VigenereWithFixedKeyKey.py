class VigenereWithFixedKeyKEY:
    def __init__(self):
        self._key_vals = [10, 4, 24]

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                key_val = self._key_vals[key_index % len(self._key_vals)]
                base = ord('A') if char.isupper() else ord('a')
                pos = ord(char) - base
                result.append(chr((pos + key_val) % 26 + base))
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                key_val = self._key_vals[key_index % len(self._key_vals)]
                base = ord('A') if char.isupper() else ord('a')
                pos = ord(char) - base
                result.append(chr((pos - key_val) % 26 + base))
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)
