class Base36SingleDigitSubstitution:
    def __init__(self):
        self._enc_map_lower = {}
        self._dec_map_lower = {}
        for i in range(26):
            ch = chr(ord('a') + i)
            if i < 10:
                mapped = chr(ord('0') + i)
            else:
                mapped = chr(ord('a') + (i - 10))
            self._enc_map_lower[ch] = mapped
            self._dec_map_lower[mapped] = ch

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                mapped = self._enc_map_lower[lower]
                if ch.isupper() and mapped.isalpha():
                    mapped = mapped.upper()
                result.append(mapped)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isdigit():
                result.append(self._dec_map_lower[ch])
            elif 'a' <= ch <= 'p':
                lower = self._dec_map_lower[ch]
                result.append(chr(ord(lower.upper())))
            elif 'A' <= ch <= 'P':
                lower = self._dec_map_lower[ch.lower()]
                result.append(lower.upper())
            else:
                result.append(ch)
        return "".join(result)
