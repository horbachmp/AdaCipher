class Base64WithAlphabetShift:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        self.shifted = self.alphabet[1:] + self.alphabet[:1]
        self.encrypt_map = {self.alphabet[i]: self.shifted[i] for i in range(64)}
        self.decrypt_map = {self.shifted[i]: self.alphabet[i] for i in range(64)}

    def encrypt(self, plaintext: str) -> str:
        import base64
        b64 = base64.b64encode(plaintext.encode("utf-8")).decode("ascii")
        return "".join(self.encrypt_map.get(ch, ch) for ch in b64)

    def decrypt(self, ciphertext: str) -> str:
        import base64
        b64 = "".join(self.decrypt_map.get(ch, ch) for ch in ciphertext)
        return base64.b64decode(b64.encode("ascii")).decode("utf-8")
