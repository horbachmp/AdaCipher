class Base64WordCipher:
    def __init__(self):
        import base64
        import re
        self._base64 = base64
        self._re = re

    def encrypt(self, plaintext: str) -> str:
        result = []
        i = 0
        n = len(plaintext)
        while i < n:
            if plaintext[i].isalpha():
                j = i
                while j < n and plaintext[j].isalpha():
                    j += 1
                word = plaintext[i:j]
                encoded = self._base64.b64encode(word.encode("utf-8")).decode("ascii").rstrip("=")
                result.append(encoded)
                i = j
            else:
                result.append(plaintext[i])
                i += 1
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        i = 0
        n = len(ciphertext)
        while i < n:
            if ciphertext[i].isalnum():
                j = i
                while j < n and ciphertext[j].isalnum():
                    j += 1
                token = ciphertext[i:j]
                pad_len = (-len(token)) % 4
                padded = token + ("=" * pad_len)
                try:
                    decoded = self._base64.b64decode(padded.encode("ascii"), validate=True).decode("utf-8")
                    if decoded.isalpha():
                        result.append(decoded)
                    else:
                        result.append(token)
                except Exception:
                    result.append(token)
                i = j
            else:
                result.append(ciphertext[i])
                i += 1
        return "".join(result)
