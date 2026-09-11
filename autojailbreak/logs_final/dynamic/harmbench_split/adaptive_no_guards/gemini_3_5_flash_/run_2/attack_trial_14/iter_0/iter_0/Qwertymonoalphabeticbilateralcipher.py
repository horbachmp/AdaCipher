class QwertyMonoalphabeticBilateralCipher:
    def __init__(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        qwerty = "qwertyuiopasdfghjklzxcvbnm"
        self.enc_lower = str.maketrans(alphabet, qwerty)
        self.dec_lower = str.maketrans(qwerty, alphabet)
        self.enc_upper = str.maketrans(alphabet.upper(), qwerty.upper())
        self.dec_upper = str.maketrans(qwerty.upper(), alphabet.upper())

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.islower():
                result.append(ch.translate(self.enc_lower))
            elif ch.isupper():
                result.append(ch.translate(self.enc_upper))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.islower():
                result.append(ch.translate(self.dec_lower))
            elif ch.isupper():
                result.append(ch.translate(self.dec_upper))
            else:
                result.append(ch)
        return "".join(result)
