class VowelConsonantInterleaveSimple:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        i = 0
        n = len(plaintext)
        while i < n:
            if plaintext[i].isalpha():
                j = i
                while j < n and plaintext[j].isalpha():
                    j += 1
                word = plaintext[i:j]
                half = (len(word) + 1) // 2
                part1 = word[:half]
                part2 = word[half:][::-1]
                result.append(part1 + "-" + part2)
                i = j
            else:
                result.append(plaintext[i])
                i += 1
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            if ciphertext[i].isalpha():
                j = i
                while j < n and ciphertext[j].isalpha():
                    j += 1
                if j < n and ciphertext[j] == "-" and j > i:
                    k = j + 1
                    while k < n and ciphertext[k].isalpha():
                        k += 1
                    part1 = ciphertext[i:j]
                    part2_reversed = ciphertext[j + 1:k]
                    result.append(part1 + part2_reversed[::-1])
                    i = k
                else:
                    result.append(ciphertext[i])
                    i += 1
            else:
                result.append(ciphertext[i])
                i += 1
        return "".join(result)
