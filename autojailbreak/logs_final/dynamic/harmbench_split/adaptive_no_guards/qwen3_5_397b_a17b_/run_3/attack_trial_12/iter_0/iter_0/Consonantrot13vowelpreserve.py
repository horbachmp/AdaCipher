class ConsonantRot13VowelPreserve:
    def __init__(self):
        lower_consonants = "bcdfghjklmnpqrstvwxyz"
        upper_consonants = lower_consonants.upper()
        shifted = lower_consonants[13:] + lower_consonants[:13]
        shifted_upper = shifted.upper()
        self.enc_map = {c: s for c, s in zip(lower_consonants, shifted)}
        self.enc_map.update({c: s for c, s in zip(upper_consonants, shifted_upper)})
        self.dec_map = {v: k for k, v in self.enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.dec_map.get(ch, ch) for ch in ciphertext)
