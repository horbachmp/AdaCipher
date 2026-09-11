class Rot5AndRot18Cipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if 'A' <= ch <= 'Z':
                out.append(chr((ord(ch) - ord('A') + 18) % 26 + ord('A')))
            elif 'a' <= ch <= 'z':
                out.append(chr((ord(ch) - ord('a') + 18) % 26 + ord('a')))
            elif '0' <= ch <= '9':
                out.append(chr((ord(ch) - ord('0') + 5) % 10 + ord('0')))
            else:
                out.append(ch)
        return ''.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if 'A' <= ch <= 'Z':
                out.append(chr((ord(ch) - ord('A') + 8) % 26 + ord('A')))
            elif 'a' <= ch <= 'z':
                out.append(chr((ord(ch) - ord('a') + 8) % 26 + ord('a')))
            elif '0' <= ch <= '9':
                out.append(chr((ord(ch) - ord('0') + 5) % 10 + ord('0')))
            else:
                out.append(ch)
        return ''.join(out)
