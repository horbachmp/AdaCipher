class A1Z26WithDashSeparator:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        n = len(plaintext)
        for i, ch in enumerate(plaintext.lower()):
            if 'a' <= ch <= 'z':
                result.append(str(ord(ch) - ord('a') + 1))
                if i + 1 < n and plaintext.lower()[i + 1].isalpha():
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
                segment = ciphertext[i:j]
                if j < n and ciphertext[j] == '-':
                    nums = [segment]
                    k = j
                    valid = True
                    while k < n and ciphertext[k] == '-':
                        k += 1
                        if k >= n or not ciphertext[k].isdigit():
                            valid = False
                            break
                        m = k
                        while m < n and ciphertext[m].isdigit():
                            m += 1
                        nums.append(ciphertext[k:m])
                        k = m
                        if k < n and ciphertext[k] != '-':
                            break
                    if valid and len(nums) > 1:
                        try:
                            letters = []
                            for num in nums:
                                val = int(num)
                                if 1 <= val <= 26:
                                    letters.append(chr(ord('a') + val - 1))
                                else:
                                    raise ValueError
                            result.append(''.join(letters))
                            i = k
                            continue
                        except ValueError:
                            pass
                try:
                    val = int(segment)
                    if 1 <= val <= 26:
                        result.append(chr(ord('a') + val - 1))
                    else:
                        result.append(segment)
                except ValueError:
                    result.append(segment)
                i = j
            else:
                result.append(ch)
                i += 1
        return ''.join(result)
