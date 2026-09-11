class AlternatingCaseAtbash:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        alpha_index = 0
        for ch in plaintext:
            if ch.isalpha():
                if ch.islower():
                    base = ord('a')
                    offset = ord(ch) - base
                else:
                    base = ord('A')
                    offset = ord(ch) - base
                if alpha_index % 2 == 0:
                    new_offset = 25 - offset
                else:
                    new_offset = (offset + 5) % 26
                result.append(chr(base + new_offset))
                alpha_index += 1
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        alpha_index = 0
        for ch in ciphertext:
            if ch.isalpha():
                if ch.islower():
                    base = ord('a')
                    offset = ord(ch) - base
                else:
                    base = ord('A')
                    offset = ord(ch) - base
                if alpha_index % 2 == 0:
                    new_offset = 25 - offset
                else:
                    new_offset = (offset - 5) % 26
                result.append(chr(base + new_offset))
                alpha_index += 1
            else:
                result.append(ch)
        return ''.join(result)
