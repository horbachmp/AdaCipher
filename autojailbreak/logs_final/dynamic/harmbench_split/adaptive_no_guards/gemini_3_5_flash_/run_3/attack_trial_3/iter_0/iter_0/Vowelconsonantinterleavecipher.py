class VowelConsonantInterleaveCipher:
    def __init__(self):
        self.lower_vowels = ['a', 'e', 'i', 'o', 'u']
        self.upper_vowels = ['A', 'E', 'I', 'O', 'U']
        self.lower_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        self.upper_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

        self.encrypt_map = {}
        self.decrypt_map = {}

        for seq in (self.lower_vowels, self.upper_vowels, self.lower_consonants, self.upper_consonants):
            n = len(seq)
            for i, ch in enumerate(seq):
                enc = seq[(i + 1) % n]
                dec = seq[(i - 1) % n]
                self.encrypt_map[ch] = enc
                self.decrypt_map[ch] = dec

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self.encrypt_map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(self.decrypt_map.get(ch, ch) for ch in ciphertext)
