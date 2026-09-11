class QwertyAtbashHybridCipher:
    def __init__(self):
        self._alphabet = "abcdefghijklmnopqrstuvwxyz"
        self._reversed_qwerty = "mnbvcxzlkjhgfdsapoiuytrewq"
        self._enc_map = {a: b for a, b in zip(self._alphabet, self._reversed_qwerty)}
        self._dec_map = {b: a for a, b in zip(self._alphabet, self._reversed_qwerty)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                mapped = self._enc_map[ch.lower()]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                mapped = self._dec_map[ch.lower()]
                result.append(mapped.upper() if ch.isupper() else mapped)
            else:
                result.append(ch)
        return "".join(result)
