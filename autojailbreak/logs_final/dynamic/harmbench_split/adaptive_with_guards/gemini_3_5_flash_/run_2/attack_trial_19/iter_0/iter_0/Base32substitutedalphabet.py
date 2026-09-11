class Base32SubstitutedAlphabet:
    def __init__(self):
        self._enc_map = {
            "a": "a1", "b": "a2", "c": "a3", "d": "a4",
            "e": "b1", "f": "b2", "g": "b3", "h": "b4",
            "i": "c1", "j": "c2", "k": "c3", "l": "c4",
            "m": "d1", "n": "d2", "o": "d3", "p": "d4",
            "q": "e1", "r": "e2", "s": "e3", "t": "e4",
            "u": "f1", "v": "f2", "w": "f3", "x": "f4",
            "y": "g1", "z": "g2",
        }
        self._dec_map = {v: k for k, v in self._enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                result.append(self._enc_map[ch.lower()])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch.isalpha() and i + 1 < n:
                pair = ch + ciphertext[i + 1]
                if pair in self._dec_map:
                    result.append(self._dec_map[pair])
                    i += 2
                    continue
            result.append(ch)
            i += 1
        return "".join(result)
