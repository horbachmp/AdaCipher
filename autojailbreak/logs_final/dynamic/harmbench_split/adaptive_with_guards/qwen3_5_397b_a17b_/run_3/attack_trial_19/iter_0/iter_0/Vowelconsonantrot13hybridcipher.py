class VowelConsonantRot13HybridCipher:
    def __init__(self):
        self._vowels = "aeiou"
        self._consonants = "bcdfghjklmnpqrstvwxyz"

    def _transform(self, text: str, direction: int) -> str:
        result = []
        for ch in text:
            if ch.isalpha():
                is_upper = ch.isupper()
                low = ch.lower()
                if low in self._vowels:
                    idx = self._vowels.index(low)
                    new_ch = self._vowels[(idx + direction * 2) % len(self._vowels)]
                else:
                    idx = self._consonants.index(low)
                    new_ch = self._consonants[(idx + direction * 10) % len(self._consonants)]
                result.append(new_ch.upper() if is_upper else new_ch)
            else:
                result.append(ch)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext, 1)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext, -1)
