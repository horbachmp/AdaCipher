class QwertyMirrorCipher:
    def __init__(self):
        standard = "abcdefghijklmnopqrstuvwxyz"
        reversed_qwerty = "mnbvcxzlkjhgfdsaqpoiuytrew"
        self.enc_lower = {a: b for a, b in zip(standard, reversed_qwerty)}
        self.dec_lower = {b: a for a, b in zip(standard, reversed_qwerty)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                mapped = self.enc_lower[ch.lower()]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                mapped = self.dec_lower[ch.lower()]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
