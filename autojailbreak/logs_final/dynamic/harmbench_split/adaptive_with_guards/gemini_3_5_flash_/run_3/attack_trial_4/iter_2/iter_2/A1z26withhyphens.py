class A1Z26WithHyphens:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        n = len(plaintext)
        for i, ch in enumerate(plaintext):
            if ch.isalpha():
                result.append(str(ord(ch.lower()) - ord('a') + 1))
                if i + 1 < n and plaintext[i + 1].isalpha():
                    result.append('-')
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch.isdigit():
                j = i
                while j < n and ciphertext[j].isdigit():
                    j += 1
                num = int(ciphertext[i:j])
                if 1 <= num <= 26:
                    result.append(chr(ord('a') + num - 1))
                    if j < n and ciphertext[j] == '-':
                        i = j + 1
                    else:
                        i = j
                else:
                    result.append(ciphertext[i:j])
                    i = j
            else:
                result.append(ch)
                i += 1
        return ''.join(result)
