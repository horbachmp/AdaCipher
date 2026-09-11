class Rot13WithVowelCaseFlipAndDigitShift:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                if 'a' <= ch <= 'z':
                    shifted = chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
                else:
                    shifted = chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
                if shifted in self.vowels:
                    shifted = shifted.swapcase()
                result.append(shifted)
            elif ch.isdigit():
                result.append(chr((ord(ch) - ord('0') + 5) % 10 + ord('0')))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                if ch in self.vowels:
                    flipped = ch.swapcase()
                else:
                    flipped = ch
                if 'a' <= flipped <= 'z':
                    decrypted = chr((ord(flipped) - ord('a') + 13) % 26 + ord('a'))
                else:
                    decrypted = chr((ord(flipped) - ord('A') + 13) % 26 + ord('A'))
                result.append(decrypted)
            elif ch.isdigit():
                result.append(chr((ord(ch) - ord('0') - 5) % 10 + ord('0')))
            else:
                result.append(ch)
        return "".join(result)
