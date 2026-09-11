class FixedKeywordSubstitution:
    def __init__(self):
        self.standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        keyword = "CIPHER"
        seen = set()
        cipher_letters = []
        for ch in keyword:
            if ch not in seen:
                seen.add(ch)
                cipher_letters.append(ch)
        for ch in self.standard:
            if ch not in seen:
                seen.add(ch)
                cipher_letters.append(ch)
        self.cipher = "".join(cipher_letters)
        self.enc_map = {self.standard[i]: self.cipher[i] for i in range(26)}
        self.dec_map = {self.cipher[i]: self.standard[i] for i in range(26)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                up = ch.upper()
                mapped = self.enc_map[up]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                up = ch.upper()
                mapped = self.dec_map[up]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)
