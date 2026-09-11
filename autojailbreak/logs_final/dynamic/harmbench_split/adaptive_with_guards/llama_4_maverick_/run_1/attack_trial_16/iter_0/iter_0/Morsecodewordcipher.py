class MorseCodeWordCipher:
    def __init__(self):
        self._encode = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.'
        }
        self._decode = {v: k for k, v in self._encode.items()}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for token in plaintext.split(' '):
            if token == '':
                continue
            if all(ch.isalnum() for ch in token):
                out.append(' '.join(self._encode[ch.upper()] for ch in token))
            else:
                out.append(token)
        return ' / '.join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for token in ciphertext.split(' / '):
            if token == '':
                continue
            parts = token.split(' ')
            if len(parts) == 1 and parts[0] and parts[0] in self._decode:
                out.append(self._decode[parts[0]])
            elif all(part in self._decode for part in parts if part):
                out.append(''.join(self._decode[part] for part in parts if part))
            else:
                out.append(token)
        return ' '.join(out)
