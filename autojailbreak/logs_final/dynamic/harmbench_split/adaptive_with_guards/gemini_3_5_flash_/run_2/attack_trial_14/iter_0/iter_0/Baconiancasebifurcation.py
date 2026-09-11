class BaconianCaseBifurcation:
    def __init__(self):
        self._encode_digit = {0: "x", 1: "X", 2: "o", 3: "O", 4: "v"}
        self._decode_digit = {"x": 0, "X": 1, "o": 2, "O": 3, "v": 4}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                idx = ord(ch.lower()) - ord("a")
                first = idx // 5
                second = idx % 5
                if first > 4:
                    first = 4
                    second = 0
                result.append(self._encode_digit[first] + self._encode_digit[second])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch in self._decode_digit and i + 1 < n and ciphertext[i + 1] in self._decode_digit:
                first = self._decode_digit[ciphertext[i]]
                second = self._decode_digit[ciphertext[i + 1]]
                idx = first * 5 + second
                if 0 <= idx < 26:
                    result.append(chr(ord("a") + idx))
                    i += 2
                    continue
            result.append(ch)
            i += 1
        return "".join(result)
