class Rot13WithVowelFlip:
    def __init__(self):
        self._vowels = set("AEIOUaeiou")

    def _rot13(self, char: str) -> str:
        if "a" <= char <= "z":
            return chr((ord(char) - ord("a") + 13) % 26 + ord("a"))
        if "A" <= char <= "Z":
            return chr((ord(char) - ord("A") + 13) % 26 + ord("A"))
        return char

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                shifted = self._rot13(char)
                if shifted in self._vowels:
                    shifted = shifted.swapcase()
                result.append(shifted)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char.isalpha():
                if char in self._vowels:
                    char = char.swapcase()
                result.append(self._rot13(char))
            else:
                result.append(char)
        return "".join(result)
