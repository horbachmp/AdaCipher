class A1Z26WithHyphens:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        plaintext = plaintext.lower()
        result = []
        for i, char in enumerate(plaintext):
            if 'a' <= char <= 'z':
                result.append(str(ord(char) - ord('a') + 1))
                if i + 1 < len(plaintext) and plaintext[i + 1].isalpha():
                    result.append('-')
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for word in ciphertext.split(' '):
            parts = word.split('-')
            decoded_parts = []
            for part in parts:
                if part.isdigit():
                    n = int(part)
                    if 1 <= n <= 26:
                        decoded_parts.append(chr(ord('a') + n - 1))
                    else:
                        decoded_parts.append(part)
                else:
                    decoded_parts.append(part)
            result.append(''.join(decoded_parts))
        return ' '.join(result)
