class ReverseAlphabetAndCaseSwap:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    rev = chr(ord('z') - (ord(char) - ord('a')))
                    result.append(rev.upper())
                else:
                    rev = chr(ord('Z') - (ord(char) - ord('A')))
                    result.append(rev.lower())
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for char in ciphertext:
            if char.isalpha():
                swapped = char.swapcase()
                if swapped.islower():
                    result.append(chr(ord('z') - (ord(swapped) - ord('a'))))
                else:
                    result.append(chr(ord('Z') - (ord(swapped) - ord('A'))))
            else:
                result.append(char)
        return "".join(result)
