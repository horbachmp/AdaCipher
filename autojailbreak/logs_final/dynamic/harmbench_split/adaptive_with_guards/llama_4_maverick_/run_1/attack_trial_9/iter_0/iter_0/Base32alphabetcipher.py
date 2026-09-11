class Base32AlphabetCipher:
    def __init__(self):
        self.alphabet = '9876543210abcdefghijklmnopqrstuv'
        self.decode_map = {ch: i for i, ch in enumerate(self.alphabet)}

    def encrypt(self, plaintext: str) -> str:
        data = plaintext.encode('utf-8')
        bit_string = ''.join(f'{byte:08b}' for byte in data)
        padding = (-len(bit_string)) % 5
        if padding:
            bit_string += '0' * padding
        ciphertext = []
        for i in range(0, len(bit_string), 5):
            chunk = bit_string[i:i + 5]
            ciphertext.append(self.alphabet[int(chunk, 2)])
        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        bit_string = ''.join(f'{self.decode_map[ch]:05b}' for ch in ciphertext)
        trunc_len = (len(bit_string) // 8) * 8
        bit_string = bit_string[:trunc_len]
        data = bytearray()
        for i in range(0, len(bit_string), 8):
            data.append(int(bit_string[i:i + 8], 2))
        return data.decode('utf-8')
