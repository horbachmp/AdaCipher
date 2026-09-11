class ConsonantVowelCaseInverter:
    def __init__(self):
        self._lower_vowels = set("aeiou")
        self._upper_vowels = set("AEIOU")

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            if char in self._lower_vowels:
                result.append(char.upper())
            elif char in self._upper_vowels:
                result.append(char.lower())
            else:
                result.append(char)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
