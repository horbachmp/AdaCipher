class WordReversalCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        word = ""

        for char in plaintext:
            if char.isalpha():
                word += char
            else:
                ciphertext += word[::-1]
                word = ""
                ciphertext += char

        # Handle the final word if the text ends with a letter
        ciphertext += word[::-1]

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        word = ""

        for char in ciphertext:
            if char.isalpha():
                word += char
            else:
                plaintext += word[::-1]
                word = ""
                plaintext += char

        # Handle the final word if the text ends with a letter
        plaintext += word[::-1]

        return plaintext
