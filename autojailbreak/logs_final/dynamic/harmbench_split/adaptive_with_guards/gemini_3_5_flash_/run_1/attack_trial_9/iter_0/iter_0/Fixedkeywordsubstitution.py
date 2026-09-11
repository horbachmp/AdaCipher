class FixedKeywordSubstitution:
    def __init__(self):
        keyword = "SECURE"
        standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cipher_alphabet = []
        seen = set()
        for ch in keyword:
            ch = ch.upper()
            if ch.isalpha() and ch not in seen:
                seen.add(ch)
                cipher_alphabet.append(ch)
        for ch in standard:
            if ch not in seen:
                cipher_alphabet.append(ch)
        self.encrypt_map_upper = {standard[i]: cipher_alphabet[i] for i in range(26)}
        self.decrypt_map_upper = {cipher_alphabet[i]: standard[i] for i in range(26)}
        self.encrypt_map_lower = {k.lower(): v.lower() for k, v in self.encrypt_map_upper.items()}
        self.decrypt_map_lower = {k.lower(): v.lower() for k, v in self.decrypt_map_upper.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isupper() and char in self.encrypt_map_upper:
                result.append(self.encrypt_map_upper[char])
            elif char.islower() and char in self.encrypt_map_lower:
                result.append(self.encrypt_map_lower[char])
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char.isupper() and char in self.decrypt_map_upper:
                result.append(self.decrypt_map_upper[char])
            elif char.islower() and char in self.decrypt_map_lower:
                result.append(self.decrypt_map_lower[char])
            else:
                result.append(char)
        return "".join(result)
