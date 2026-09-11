class Rot13WithVowelConsonantCaseFlipAndDigitShift:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        vowels = set("AEIOUaeiou")
        for char in plaintext:
            if char.isalpha():
                shifted = chr((ord(char.lower()) - ord('a') + 13) % 26 + ord('a'))
                if shifted in vowels:
                    shifted = shifted.swapcase()
                result.append(shifted)
            elif char.isdigit():
                result.append(str((int(char) + 5) % 10))
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        vowels = set("AEIOUaeiou")
        for char in ciphertext:
            if char.isalpha():
                if char in vowels:
                    char = char.swapcase()
                result.append(chr((ord(char.lower()) - ord('a') + 13) % 26 + ord('a')))
            elif char.isdigit():
                result.append(str((int(char) - 5) % 10))
            else:
                result.append(char)
        return "".join(result)
