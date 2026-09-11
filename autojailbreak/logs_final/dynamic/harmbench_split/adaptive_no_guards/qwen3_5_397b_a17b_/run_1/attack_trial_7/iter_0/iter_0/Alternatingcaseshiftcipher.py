class AlternatingCaseShiftCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        alpha_index = 0
        for char in plaintext:
            if char.isalpha():
                alpha_index += 1
                base = ord('A') if char.isupper() else ord('a')
                offset = ord(char) - base
                if alpha_index % 2 == 1:
                    offset = (offset + 1) % 26
                else:
                    offset = (offset - 1) % 26
                result.append(chr(base + offset))
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        alpha_index = 0
        for char in ciphertext:
            if char.isalpha():
                alpha_index += 1
                base = ord('A') if char.isupper() else ord('a')
                offset = ord(char) - base
                if alpha_index % 2 == 1:
                    offset = (offset - 1) % 26
                else:
                    offset = (offset + 1) % 26
                result.append(chr(base + offset))
            else:
                result.append(char)
        return "".join(result)
