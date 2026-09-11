class AlternatingCaseShiftCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for i, char in enumerate(plaintext):
            if not (("A" <= char <= "Z") or ("a" <= char <= "z")):
                result.append(char)
                continue
            shift = 3 if i % 2 == 0 else -3
            base = 97 if char.islower() else 65
            result.append(chr((ord(char) - base + shift) % 26 + base))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for i, char in enumerate(ciphertext):
            if not (("A" <= char <= "Z") or ("a" <= char <= "z")):
                result.append(char)
                continue
            shift = -3 if i % 2 == 0 else 3
            base = 97 if char.islower() else 65
            result.append(chr((ord(char) - base + shift) % 26 + base))
        return "".join(result)
