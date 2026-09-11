class VowelSubstitutionCipher:
    def __init__(self):
        self.enc_lower = str.maketrans({'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'})
        self.enc_upper = str.maketrans({'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'})
        self.dec_lower = str.maketrans({'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o', 'a': 'u'})
        self.dec_upper = str.maketrans({'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O', 'A': 'U'})

    def encrypt(self, plaintext: str) -> str:
        return plaintext.translate(self.enc_lower).translate(self.enc_upper)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext.translate(self.dec_lower).translate(self.dec_upper)
