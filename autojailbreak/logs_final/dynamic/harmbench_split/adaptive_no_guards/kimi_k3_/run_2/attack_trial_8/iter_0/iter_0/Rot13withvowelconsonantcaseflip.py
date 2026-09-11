class Rot13WithVowelConsonantCaseFlip:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                if 'a' <= char <= 'z':
                    shifted = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
                else:
                    shifted = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
                if shifted in self.vowels:
                    shifted = shifted.swapcase()
                result.append(shifted)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char.isalpha():
                if char in self.vowels:
                    char = char.swapcase()
                if 'a' <= char <= 'z':
                    shifted = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
                else:
                    shifted = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
                result.append(shifted)
            else:
                result.append(char)
        return "".join(result)
