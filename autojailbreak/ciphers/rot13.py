class ROT13Cipher:
    def __init__(self):
        self.shift = 13

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""

        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    base = ord('a')
                else:
                    base = ord('A')

                ciphertext += chr(
                    (ord(char) - base + self.shift) % 26 + base
                )
            else:
                ciphertext += char

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""

        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    base = ord('a')
                else:
                    base = ord('A')

                plaintext += chr(
                    (ord(char) - base + self.shift) % 26 + base
                )
            else:
                plaintext += char

        return plaintext
