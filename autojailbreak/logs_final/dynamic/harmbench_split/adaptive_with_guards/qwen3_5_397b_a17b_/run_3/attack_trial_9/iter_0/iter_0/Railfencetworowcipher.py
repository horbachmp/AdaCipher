class RailFenceTwoRowCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        part_a = plaintext[0::2]
        part_b = plaintext[1::2]
        return part_a + "|" + part_b

    def decrypt(self, ciphertext: str) -> str:
        if "|" not in ciphertext:
            raise ValueError("Invalid ciphertext format")
        part_a, part_b = ciphertext.split("|", 1)
        result = []
        len_a = len(part_a)
        len_b = len(part_b)
        i = j = 0
        total = len_a + len_b
        for idx in range(total):
            if idx % 2 == 0:
                if i < len_a:
                    result.append(part_a[i])
                    i += 1
            else:
                if j < len_b:
                    result.append(part_b[j])
                    j += 1
        return "".join(result)
