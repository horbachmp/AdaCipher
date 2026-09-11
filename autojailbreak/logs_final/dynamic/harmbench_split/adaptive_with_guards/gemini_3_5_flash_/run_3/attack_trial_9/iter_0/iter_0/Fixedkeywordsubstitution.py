class FixedKeywordSubstitution:
    def __init__(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        keyword = "SECURE"
        seen = set()
        cipher_letters = []
        for ch in keyword:
            if ch not in seen:
                seen.add(ch)
                cipher_letters.append(ch)
        for ch in alphabet:
            if ch not in seen:
                cipher_letters.append(ch)
        self.encrypt_map = {plain: cipher for plain, cipher in zip(alphabet, cipher_letters)}
        self.decrypt_map = {cipher: plain for plain, cipher in self.encrypt_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                mapped = self.encrypt_map[ch.upper()]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                mapped = self.decrypt_map[ch.upper()]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)
