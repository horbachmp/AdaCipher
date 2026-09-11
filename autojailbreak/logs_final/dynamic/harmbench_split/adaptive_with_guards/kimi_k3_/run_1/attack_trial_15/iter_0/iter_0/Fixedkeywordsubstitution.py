class FixedKeywordSubstitution:
    def __init__(self):
        keyword = "CIPHER"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        seen = set()
        cipher_letters = []
        for ch in keyword:
            if ch not in seen and ch in alphabet:
                seen.add(ch)
                cipher_letters.append(ch)
        for ch in alphabet:
            if ch not in seen:
                cipher_letters.append(ch)
                seen.add(ch)
        self._enc_upper = {plain: cipher for plain, cipher in zip(alphabet, cipher_letters)}
        self._dec_upper = {cipher: plain for plain, cipher in zip(alphabet, cipher_letters)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                upper = ch.upper()
                mapped = self._enc_upper[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                upper = ch.upper()
                mapped = self._dec_upper[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return "".join(result)
