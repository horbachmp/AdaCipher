class MorseCodeWordCipher:
    def __init__(self):
        self._encode = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
        }
        self._decode = {v: k for k, v in self._encode.items()}

    def encrypt(self, plaintext: str) -> str:
        tokens = []
        for word in plaintext.split(' '):
            if word == '':
                tokens.append('/')
                continue
            if any(ch.isalpha() for ch in word):
                letters = []
                for ch in word:
                    if ch.isalpha():
                        letters.append(self._encode[ch.lower()])
                    else:
                        letters.append(ch)
                tokens.append(' '.join(letters))
            else:
                tokens.append(word)
        return ' / '.join(tokens)

    def decrypt(self, ciphertext: str) -> str:
        words = []
        for token in ciphertext.split(' / '):
            if token == '':
                words.append('')
                continue
            parts = token.split(' ')
            decoded = []
            for part in parts:
                if part in self._decode:
                    decoded.append(self._decode[part])
                else:
                    decoded.append(part)
            words.append(''.join(decoded))
        return ' '.join(words)
