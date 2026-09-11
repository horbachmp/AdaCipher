class BaconianCaseAlternatingCipher:
    def __init__(self):
        self._enc_upper = {}
        self._enc_lower = {}
        self._dec_upper = {}
        self._dec_lower = {}
        for i in range(26):
            bits = format(i, "05b")
            upper_seq = "".join("A" if b == "0" else "B" for b in bits)
            lower_seq = upper_seq.lower()
            ch_upper = chr(ord("A") + i)
            ch_lower = chr(ord("a") + i)
            self._enc_upper[ch_upper] = upper_seq
            self._enc_lower[ch_lower] = lower_seq
            self._dec_upper[upper_seq] = ch_upper
            self._dec_lower[lower_seq] = ch_lower

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.isalpha():
                if ch.isupper():
                    out.append(self._enc_upper[ch])
                else:
                    out.append(self._enc_lower[ch])
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch in "ABab" and i + 5 <= n:
                block = ciphertext[i:i + 5]
                if all(c in "AB" for c in block):
                    out.append(self._dec_upper.get(block, block))
                    i += 5
                    continue
                if all(c in "ab" for c in block):
                    out.append(self._dec_lower.get(block, block))
                    i += 5
                    continue
            out.append(ch)
            i += 1
        return "".join(out)
