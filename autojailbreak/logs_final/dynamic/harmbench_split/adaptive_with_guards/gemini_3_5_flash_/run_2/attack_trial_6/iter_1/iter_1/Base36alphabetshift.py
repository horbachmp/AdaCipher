class Base36AlphabetShift:
    def __init__(self):
        self.sequence = "abcdefghijklmnopqrstuvwxyz0123456789"
        self.index_map = {ch: i for i, ch in enumerate(self.sequence)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.islower() or ch.isdigit():
                idx = self.index_map.get(ch)
                if idx is not None:
                    new_ch = self.sequence[(idx + 5) % 36]
                    result.append(new_ch)
                else:
                    result.append(ch)
            elif ch.isupper():
                lower = ch.lower()
                idx = self.index_map.get(lower)
                if idx is not None:
                    new_ch = self.sequence[(idx + 5) % 36]
                    result.append(new_ch.upper() if new_ch.isalpha() else new_ch)
                else:
                    result.append(ch)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.islower() or ch.isdigit():
                idx = self.index_map.get(ch)
                if idx is not None:
                    new_ch = self.sequence[(idx - 5) % 36]
                    result.append(new_ch)
                else:
                    result.append(ch)
            elif ch.isupper():
                lower = ch.lower()
                idx = self.index_map.get(lower)
                if idx is not None:
                    new_ch = self.sequence[(idx - 5) % 36]
                    result.append(new_ch.upper() if new_ch.isalpha() else new_ch)
                else:
                    result.append(ch)
            else:
                result.append(ch)
        return "".join(result)
