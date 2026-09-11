class Rot13WithVowelDouble:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

    def _rot13_char(self, char: str) -> str:
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        if 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        return char

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                transformed = self._rot13_char(char)
                if transformed in self.vowels:
                    result.append(transformed * 2)
                else:
                    result.append(transformed)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        collapsed = []
        i = 0
        n = len(ciphertext)
        while i < n:
            char = ciphertext[i]
            if char in self.vowels and i + 1 < n and ciphertext[i + 1] == char:
                collapsed.append(char)
                i += 2
            else:
                collapsed.append(char)
                i += 1
        result = []
        for char in "".join(collapsed):
            if char.isalpha():
                result.append(self._rot13_char(char))
            else:
                result.append(char)
        return "".join(result)
