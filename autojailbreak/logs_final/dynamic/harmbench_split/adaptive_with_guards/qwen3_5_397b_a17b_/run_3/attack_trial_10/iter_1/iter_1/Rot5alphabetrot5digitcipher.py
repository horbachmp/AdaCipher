class Rot5AlphabetRot5DigitCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            o = ord(char)
            if 65 <= o <= 90:
                result.append(chr(((o - 65 + 5) % 26) + 65))
            elif 97 <= o <= 122:
                result.append(chr(((o - 97 + 5) % 26) + 97))
            elif 48 <= o <= 57:
                result.append(chr(((o - 48 + 5) % 10) + 48))
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            o = ord(char)
            if 65 <= o <= 90:
                result.append(chr(((o - 65 - 5) % 26) + 65))
            elif 97 <= o <= 122:
                result.append(chr(((o - 97 - 5) % 26) + 97))
            elif 48 <= o <= 57:
                result.append(chr(((o - 48 - 5) % 10) + 48))
            else:
                result.append(char)
        return "".join(result)
