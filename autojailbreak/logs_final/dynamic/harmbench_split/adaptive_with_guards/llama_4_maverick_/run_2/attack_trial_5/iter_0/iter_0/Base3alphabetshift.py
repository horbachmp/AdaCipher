class Base3AlphabetShift:
    def __init__(self):
        self.encode_map = {'0': 'd', '1': 'f', '2': 'g'}
        self.decode_map = {'d': '0', 'f': '1', 'g': '2', 'D': '0', 'F': '1', 'G': '2'}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.isalpha():
                idx = ord(ch.lower()) - ord('a')
                trits = format(idx, '03b')
                trits = trits.replace('0', '0').replace('1', '1')
                base3 = ""
                n = idx
                digits = []
                for _ in range(3):
                    digits.append(str(n % 3))
                    n //= 3
                base3 = ''.join(reversed(digits))
                encoded = ''.join(self.encode_map[d] for d in base3)
                out.append(encoded.upper() if ch.isupper() else encoded.lower())
            else:
                out.append(ch)
        return ''.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        i = 0
        while i < len(ciphertext):
            ch = ciphertext[i]
            if ch.isalpha():
                if i + 2 < len(ciphertext) and ciphertext[i + 1].isalpha() and ciphertext[i + 2].isalpha():
                    block = ciphertext[i:i + 3]
                    digits = []
                    for c in block:
                        if c not in self.decode_map:
                            digits = None
                            break
                        digits.append(self.decode_map[c])
                    if digits is not None:
                        idx = int(''.join(digits), 3)
                        letter = chr(idx + ord('A')) if block[0].isupper() else chr(idx + ord('a'))
                        out.append(letter)
                        i += 3
                        continue
                out.append(ch)
            else:
                out.append(ch)
            i += 1
        return ''.join(out)
