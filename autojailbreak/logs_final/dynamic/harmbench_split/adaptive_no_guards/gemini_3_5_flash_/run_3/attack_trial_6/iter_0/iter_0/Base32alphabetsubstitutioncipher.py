class Base32AlphabetSubstitutionCipher:
    def __init__(self):
        self.enc_map = {
            'A': 'A1', 'B': 'B2', 'C': 'C3', 'D': 'D4', 'E': 'E5', 'F': 'F6', 'G': 'G7',
            'H': 'H8', 'I': 'I9', 'J': 'J0', 'K': 'K1', 'L': 'L2', 'M': 'M3', 'N': 'N4',
            'O': 'O5', 'P': 'P6', 'Q': 'Q7', 'R': 'R8', 'S': 'S9', 'T': 'T0', 'U': 'U1',
            'V': 'V2', 'W': 'W3', 'X': 'X4', 'Y': 'Y5', 'Z': 'Z6'
        }
        self.dec_map = {v: k for k, v in self.enc_map.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                code = self.enc_map[ch.upper()]
                if ch.islower():
                    code = code[0].lower() + code[1]
                result.append(code)
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        while i < len(ciphertext):
            if i + 1 < len(ciphertext) and ciphertext[i].isalpha() and ciphertext[i + 1].isdigit():
                key = ciphertext[i].upper() + ciphertext[i + 1]
                if key in self.dec_map:
                    letter = self.dec_map[key]
                    if ciphertext[i].islower():
                        letter = letter.lower()
                    result.append(letter)
                    i += 2
                    continue
            result.append(ciphertext[i])
            i += 1
        return ''.join(result)
