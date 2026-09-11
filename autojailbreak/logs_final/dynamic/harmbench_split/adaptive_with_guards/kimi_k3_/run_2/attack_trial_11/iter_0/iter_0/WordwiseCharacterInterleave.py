class WordwiseCharacterInterleave:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        parts = plaintext.split(' ')
        encrypted_parts = []
        for word in parts:
            if word == '':
                encrypted_parts.append(word)
                continue
            n = len(word)
            split_point = (n + 1) // 2
            part_a = word[:split_point]
            part_b = word[split_point:]
            encrypted_parts.append(part_a + '-' + part_b[::-1])
        return ' '.join(encrypted_parts)

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split(' ')
        decrypted_parts = []
        for word in parts:
            if '-' in word:
                part_a, part_b_reversed = word.split('-', 1)
                decrypted_parts.append(part_a + part_b_reversed[::-1])
            else:
                decrypted_parts.append(word)
        return ' '.join(decrypted_parts)
