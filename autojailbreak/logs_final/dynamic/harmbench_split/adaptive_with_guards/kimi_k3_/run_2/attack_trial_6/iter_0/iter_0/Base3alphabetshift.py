class Base3AlphabetShift:
    def __init__(self):
        self._encode_map = {0: "aaa", 1: "aab", 2: "aac", 3: "aba", 4: "abb", 5: "abc", 6: "aca", 7: "acb", 8: "acc", 9: "baa", 10: "bab", 11: "bac", 12: "bba", 13: "bbb", 14: "bbc", 15: "bca", 16: "bcb", 17: "bcc", 18: "caa", 19: "cab", 20: "cac", 21: "cba", 22: "cbb", 23: "cbc", 24: "cca", 25: "ccb"}
        self._decode_map = {v: k for k, v in self._encode_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                idx = ord(ch.lower()) - ord('a')
                block = self._encode_map[idx]
                if ch.isupper():
                    block = block.upper()
                result.append(block)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            ch = ciphertext[i]
            if ch.isalpha():
                block_chars = [ch]
                j = i + 1
                while j < n and len(block_chars) < 3:
                    if ciphertext[j].isalpha():
                        block_chars.append(ciphertext[j])
                    j += 1
                if len(block_chars) == 3:
                    block = "".join(block_chars)
                    lower_block = block.lower()
                    if lower_block in self._decode_map:
                        val = self._decode_map[lower_block]
                        letter = chr(ord('a') + val)
                        if block.isupper():
                            letter = letter.upper()
                        result.append(letter)
                        i = j
                        continue
                result.append(ch)
                i += 1
            else:
                result.append(ch)
                i += 1
        return "".join(result)
