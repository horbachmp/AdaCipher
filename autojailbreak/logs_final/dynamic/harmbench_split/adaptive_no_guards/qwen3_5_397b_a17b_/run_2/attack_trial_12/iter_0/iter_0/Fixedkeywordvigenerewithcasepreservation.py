class FixedKeywordVigenereWithCasePreservation:
    def __init__(self):
        self._shifts = [2, 8, 15, 7, 4, 17]

    def encrypt(self, plaintext: str) -> str:
        result = []
        idx = 0
        for ch in plaintext:
            if ch.isalpha():
                shift = self._shifts[idx % len(self._shifts)]
                base = ord('a') if ch.islower() else ord('A')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
                idx += 1
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        idx = 0
        for ch in ciphertext:
            if ch.isalpha():
                shift = self._shifts[idx % len(self._shifts)]
                base = ord('a') if ch.islower() else ord('A')
                result.append(chr((ord(ch) - base - shift) % 26 + base))
                idx += 1
            else:
                result.append(ch)
        return "".join(result)
