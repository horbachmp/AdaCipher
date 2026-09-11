class A1Z26WithDashSeparators:
    def __init__(self):
        self._alphabet = {str(i): chr(ord('a') + i - 1) for i in range(1, 27)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        in_word = False
        for ch in plaintext:
            if ch.isalpha():
                num = str(ord(ch.lower()) - ord('a') + 1)
                if in_word:
                    result.append('-')
                result.append(num)
                in_word = True
            else:
                result.append(ch)
                in_word = False
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        token = []
        for ch in ciphertext:
            if ch.isdigit() or ch == '-':
                token.append(ch)
            else:
                if token:
                    result.append(self._decode_block(''.join(token)))
                    token = []
                result.append(ch)
        if token:
            result.append(self._decode_block(''.join(token)))
        return ''.join(result)

    def _decode_block(self, block: str) -> str:
        parts = block.split('-')
        decoded = []
        for part in parts:
            if part:
                decoded.append(self._alphabet.get(part, ''))
        return ''.join(decoded)
