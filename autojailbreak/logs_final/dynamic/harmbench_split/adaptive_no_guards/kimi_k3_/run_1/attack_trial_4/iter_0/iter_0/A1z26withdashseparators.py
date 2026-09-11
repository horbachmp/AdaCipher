class A1Z26WithDashSeparators:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        parts = []
        prev_was_letter = False
        for ch in plaintext:
            if ch.isalpha():
                code = ord(ch.upper()) - ord('A') + 1
                token = ('U' if ch.isupper() else 'L') + str(code)
                if prev_was_letter:
                    parts.append('-')
                parts.append(token)
                prev_was_letter = True
            else:
                parts.append(ch)
                prev_was_letter = False
        return ''.join(parts)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch in ('U', 'L'):
                j = i + 1
                while j < n and ciphertext[j].isdigit():
                    j += 1
                num = int(ciphertext[i + 1:j]) if j > i + 1 else None
                if num is not None and 1 <= num <= 26:
                    base = ord('A') if ch == 'U' else ord('a')
                    result.append(chr(base + num - 1))
                    i = j
                    continue
            result.append(ch)
            i += 1
        return ''.join(result)
