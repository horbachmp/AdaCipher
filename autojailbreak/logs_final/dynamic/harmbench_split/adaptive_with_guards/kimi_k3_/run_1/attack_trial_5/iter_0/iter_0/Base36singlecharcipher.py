class Base36SingleCharCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if "a" <= ch <= "z":
                idx = ord(ch) - ord("a")
                if idx < 10:
                    result.append(chr(ord("0") + idx))
                else:
                    result.append(chr(ord("a") + idx - 10))
            elif "A" <= ch <= "Z":
                idx = ord(ch) - ord("A")
                if idx < 10:
                    result.append(chr(ord("0") + idx))
                else:
                    result.append(chr(ord("A") + idx - 10))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if "0" <= ch <= "9":
                result.append(chr(ord("a") + ord(ch) - ord("0")))
            elif "a" <= ch <= "p":
                result.append(chr(ord("a") + 10 + ord(ch) - ord("a")))
            elif "A" <= ch <= "P":
                result.append(chr(ord("A") + 10 + ord(ch) - ord("A")))
            else:
                result.append(ch)
        return "".join(result)
