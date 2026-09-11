class VowelConsonantInterleaveCipher:
    def __init__(self):
        self._vowels = "AEIOU"
        self._consonants = "BCDFGHJKLMNPQRSTVWXYZ"

    def _transform_char(self, char: str, shift: int) -> str:
        if not char.isalpha():
            return char
        upper = char.upper()
        if upper in self._vowels:
            idx = self._vowels.index(upper)
            new_char = self._vowels[(idx + shift) % len(self._vowels)]
        else:
            idx = self._consonants.index(upper)
            new_char = self._consonants[(idx + shift) % len(self._consonants)]
        return new_char if char.isupper() else new_char.lower()

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._transform_char(char, 2) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._transform_char(char, -2) for char in ciphertext)
