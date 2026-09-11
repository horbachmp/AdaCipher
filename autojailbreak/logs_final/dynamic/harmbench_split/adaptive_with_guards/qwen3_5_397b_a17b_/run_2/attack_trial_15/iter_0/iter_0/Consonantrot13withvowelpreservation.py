class ConsonantRot13WithVowelPreservation:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

    def _transform(self, text: str, forward: bool) -> str:
        result = []
        for char in text:
            if char.isalpha() and char not in self.vowels:
                if char.islower():
                    base = 97
                else:
                    base = 65
                offset = 13 if forward else -13
                result.append(chr(((ord(char) - base + offset) % 26) + base))
            else:
                result.append(char)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext, True)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext, False)
