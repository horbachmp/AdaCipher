class A1Z26HyphenatedCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        prev_was_letter = False
        for ch in plaintext:
            if ch.isalpha():
                if prev_was_letter:
                    result.append("-")
                if ch.isupper():
                    result.append("u")
                else:
                    result.append("l")
                result.append(str(ord(ch.lower()) - ord("a") + 1))
                prev_was_letter = True
            else:
                result.append(ch)
                prev_was_letter = False
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if (ch == "u" or ch == "l") and i + 1 < n and ciphertext[i + 1].isdigit():
                prefix = ch
                j = i + 1
                num = []
                while j < n and ciphertext[j].isdigit():
                    num.append(ciphertext[j])
                    j += 1
                if num:
                    value = int("".join(num))
                    if 1 <= value <= 26:
                        letter = chr(ord("a") + value - 1)
                        if prefix == "u":
                            letter = letter.upper()
                        result.append(letter)
                        i = j
                        if i < n and ciphertext[i] == "-":
                            i += 1
                        continue
            result.append(ch)
            i += 1
        return "".join(result)
