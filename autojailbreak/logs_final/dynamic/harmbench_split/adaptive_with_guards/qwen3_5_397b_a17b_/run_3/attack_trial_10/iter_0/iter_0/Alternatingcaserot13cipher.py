class AlternatingCaseRot13Cipher:
    def __init__(self):
        pass

    def _rot13(self, ch: str) -> str:
        if 'a' <= ch <= 'z':
            return chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
        if 'A' <= ch <= 'Z':
            return chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        return ch

    def encrypt(self, plaintext: str) -> str:
        result = []
        alpha_counter = 1
        for ch in plaintext:
            if ch.isalpha():
                transformed = self._rot13(ch)
                if alpha_counter % 2 == 1:
                    transformed = transformed.upper()
                else:
                    transformed = transformed.lower()
                result.append(transformed)
                alpha_counter += 1
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        alpha_counter = 1
        for ch in ciphertext:
            if ch.isalpha():
                transformed = self._rot13(ch)
                if alpha_counter % 2 == 1:
                    transformed = transformed.upper()
                else:
                    transformed = transformed.lower()
                result.append(transformed)
                alpha_counter += 1
            else:
                result.append(ch)
        return ''.join(result)
