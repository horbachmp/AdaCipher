class HomoglyphLookalikeSubstitution:
    def __init__(self):
        self.enc_map = {
            'a': 'а', 'b': 'Ь', 'c': 'с', 'd': 'ԁ', 'e': 'е', 'f': 'f', 'g': 'g', 'h': 'һ', 'i': 'і', 'j': 'ј', 'k': 'к', 'l': 'l', 'm': 'm', 'n': 'ո', 'o': 'о', 'p': 'р', 'q': 'ԛ', 'r': 'r', 's': 'ѕ', 't': 't', 'u': 'ս', 'v': 'ѵ', 'w': 'ԝ', 'x': 'х', 'y': 'у', 'z': 'z',
            'A': 'А', 'B': 'В', 'C': 'С', 'D': 'D', 'E': 'Е', 'F': 'F', 'G': 'G', 'H': 'Н', 'I': 'І', 'J': 'Ј', 'K': 'К', 'L': 'L', 'M': 'М', 'N': 'N', 'O': 'О', 'P': 'Р', 'Q': 'Q', 'R': 'R', 'S': 'Ѕ', 'T': 'Т', 'U': 'U', 'V': 'Ѵ', 'W': 'W', 'X': 'Х', 'Y': 'Ү', 'Z': 'Z'
        }
        self.dec_map = {}
        for k, v in self.enc_map.items():
            self.dec_map[v] = k

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.enc_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.dec_map.get(ch, ch) for ch in ciphertext)
