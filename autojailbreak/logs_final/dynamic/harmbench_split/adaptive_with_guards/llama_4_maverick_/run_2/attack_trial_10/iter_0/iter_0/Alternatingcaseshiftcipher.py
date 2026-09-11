class AlternatingCaseShiftCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        i = 0
        for ch in plaintext:
            if ch.isalpha():
                base = ord('a') if ch.islower() else ord('A')
                if i % 2 == 0:
                    result.append(chr((ord(ch) - base + 1) % 26 + base))
                else:
                    result.append(chr((ord(ch) - base - 1) % 26 + base))
                i += 1
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        for ch in ciphertext:
            if ch.isalpha():
                base = ord('a') if ch.islower() else ord('A')
                if i % 2 == 0:
                    result.append(chr((ord(ch) - base - 1) % 26 + base))
                else:
                    result.append(chr((ord(ch) - base + 1) % 26 + base))
                i += 1
            else:
                result.append(ch)
        return "".join(result)
