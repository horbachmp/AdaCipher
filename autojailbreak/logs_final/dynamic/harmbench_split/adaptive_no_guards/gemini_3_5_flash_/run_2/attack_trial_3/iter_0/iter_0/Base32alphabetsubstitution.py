class Base32AlphabetSubstitution:
    def __init__(self):
        self.enc_map = {
            'A': 'A2', 'B': 'B3', 'C': 'C4', 'D': 'D5', 'E': 'E6', 'F': 'F7',
            'G': 'G2', 'H': 'H3', 'I': 'I4', 'J': 'J5', 'K': 'K6', 'L': 'L7',
            'M': 'M2', 'N': 'N3', 'O': 'O4', 'P': 'P5', 'Q': 'Q6', 'R': 'R7',
            'S': 'S2', 'T': 'T3', 'U': 'U4', 'V': 'V5', 'W': 'W6', 'X': 'X7',
            'Y': 'Y2', 'Z': 'Z3',
        }
        self.dec_map = {v: k for k, v in self.enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch.isalpha():
                out.append(self.enc_map[ch.upper()])
            else:
                out.append(ch)
        return ''.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        i = 0
        while i < len(ciphertext):
            ch = ciphertext[i]
            if i + 1 < len(ciphertext) and ch.isalpha() and ciphertext[i + 1] in '234567':
                pair = ch.upper() + ciphertext[i + 1]
                if pair in self.dec_map:
                    out.append(self.dec_map[pair])
                    i += 2
                    continue
            out.append(ch)
            i += 1
        return ''.join(out)
