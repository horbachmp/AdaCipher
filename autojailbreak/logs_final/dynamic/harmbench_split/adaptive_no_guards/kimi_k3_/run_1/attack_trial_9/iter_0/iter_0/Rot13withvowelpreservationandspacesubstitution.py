class Rot13WithVowelPreservationAndSpaceSubstitution:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

    def _rot13_consonant(self, char: str) -> str:
        if char.isupper():
            base = ord('A')
        else:
            base = ord('a')
        return chr((ord(char) - base + 13) % 26 + base)

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                if char in self.vowels:
                    result.append(char)
                else:
                    result.append(self._rot13_consonant(char))
            elif char == ' ':
                result.append('-')
            elif char == '-':
                result.append(' ')
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char.isalpha():
                if char in self.vowels:
                    result.append(char)
                else:
                    result.append(self._rot13_consonant(char))
            elif char == '-':
                result.append(' ')
            elif char == ' ':
                result.append('-')
            else:
                result.append(char)
        return ''.join(result)
