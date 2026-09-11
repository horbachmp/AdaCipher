class LeetRot5Cipher:
    def __init__(self):
        self.enc_vowel_map = {
            "a": "4", "e": "3", "i": "1", "o": "0", "u": "5",
            "A": "4", "E": "3", "I": "1", "O": "0", "U": "5",
        }
        self.dec_digit_map = {
            "4": "a", "3": "e", "1": "i", "0": "o", "5": "u",
        }

    def encrypt(self, plaintext: str) -> str:
        shifted = []
        for char in plaintext:
            if char.isalpha():
                base = ord("a") if char.islower() else ord("A")
                shifted.append(chr((ord(char) - base + 5) % 26 + base))
            else:
                shifted.append(char)
        result = []
        for char in "".join(shifted):
            result.append(self.enc_vowel_map.get(char, char))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        unleet = []
        for char in ciphertext:
            unleet.append(self.dec_digit_map.get(char, char))
        result = []
        for char in "".join(unleet):
            if char.isalpha():
                base = ord("a") if char.islower() else ord("A")
                result.append(chr((ord(char) - base - 5) % 26 + base))
            else:
                result.append(char)
        return "".join(result)
