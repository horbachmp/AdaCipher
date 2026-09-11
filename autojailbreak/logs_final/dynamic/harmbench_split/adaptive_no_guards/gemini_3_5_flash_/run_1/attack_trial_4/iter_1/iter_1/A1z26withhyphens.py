class A1Z26WithHyphens:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        text = plaintext.lower()
        for i, char in enumerate(text):
            if 'a' <= char <= 'z':
                result.append(str(ord(char) - ord('a') + 1))
                if i + 1 < len(text) and text[i + 1].isalpha():
                    result.append('-')
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            char = ciphertext[i]
            if char.isdigit():
                j = i
                while j < n and ciphertext[j].isdigit():
                    j += 1
                token = ciphertext[i:j]
                if token and 1 <= int(token) <= 26:
                    result.append(chr(ord('a') + int(token) - 1))
                    i = j
                    if i < n and ciphertext[i] == '-':
                        i += 1
                    continue
                result.append(token)
                i = j
            else:
                result.append(char)
                i += 1
        return ''.join(result)
