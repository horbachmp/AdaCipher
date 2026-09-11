class QwertyMonoalphabeticBypass:
    def __init__(self):
        self._enc_lower = str.maketrans("abcdefghijklmnopqrstuvwxyz", "qwertyuiopasdfghjklzxcvbnm")
        self._enc_upper = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "QWERTYUIOPASDFGHJKLZXCVBNM")
        self._dec_lower = str.maketrans("qwertyuiopasdfghjklzxcvbnm", "abcdefghijklmnopqrstuvwxyz")
        self._dec_upper = str.maketrans("QWERTYUIOPASDFGHJKLZXCVBNM", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def encrypt(self, plaintext: str) -> str:
        return plaintext.translate(self._enc_lower).translate(self._enc_upper)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext.translate(self._dec_lower).translate(self._dec_upper)
