class ConsonantRotatorWithVowelStatic:
    def __init__(self):
        lower_from = "bcdfghjklmnpqrstvwxyz"
        lower_to = "cdfghjklmnpqrstvwxyzb"
        self._enc_lower = str.maketrans(lower_from, lower_to)
        self._dec_lower = str.maketrans(lower_to, lower_from)
        upper_from = lower_from.upper()
        upper_to = lower_to.upper()
        self._enc_upper = str.maketrans(upper_from, upper_to)
        self._dec_upper = str.maketrans(upper_to, upper_from)

    def encrypt(self, plaintext: str) -> str:
        return plaintext.translate(self._enc_lower).translate(self._enc_upper)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext.translate(self._dec_lower).translate(self._dec_upper)
