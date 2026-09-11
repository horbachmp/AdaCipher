class A1Z26WordCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        current_numbers = []
        for ch in plaintext:
            if ch.isalpha():
                current_numbers.append(str(ord(ch.lower()) - ord('a') + 1))
            else:
                if current_numbers:
                    result.append("-".join(current_numbers))
                    current_numbers = []
                result.append(ch)
        if current_numbers:
            result.append("-".join(current_numbers))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        token = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch.isdigit():
                token.append(ch)
            elif ch == '-':
                if token:
                    token.append(ch)
                else:
                    result.append(ch)
            else:
                if token:
                    parts = "".join(token).split('-')
                    for part in parts:
                        if part:
                            result.append(chr(int(part) - 1 + ord('a')))
                    token = []
                result.append(ch)
            i += 1
        if token:
            parts = "".join(token).split('-')
            for part in parts:
                if part:
                    result.append(chr(int(part) - 1 + ord('a')))
        return "".join(result)
