class ConsonantRot13VowelPreserve:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        vowels = set("aeiouAEIOU")
        for ch in plaintext:
            if ch in vowels:
                result.append(ch)
            elif ch.isalpha():
                if 'a' <= ch <= 'z':
                    base = ord('a')
                else:
                    base = ord('A')
                result.append(chr((ord(ch) - base + 13) % 26 + base))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        vowels = set("aeiouAEIOU")
        for ch in ciphertext:
            if ch in vowels:
                result.append(ch)
            elif ch.isalpha():
                if 'a' <= ch <= 'z':
                    base = ord('a')
                else:
                    base = ord('A')
                result.append(chr((ord(ch) - base + 13) % 26 + base))
            else:
                result.append(ch)
        return "".join(result)
