class ConsonantRot13VowelLeet:
    def __init__(self):
        self._leet_enc = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'u': '5'}
        self._leet_dec = {'4': 'a', '3': 'e', '1': 'i', '0': 'o', '5': 'u'}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                lower = ch.lower()
                if lower in self._leet_enc:
                    result.append(self._leet_enc[lower])
                else:
                    base = ord('A') if ch.isupper() else ord('a')
                    result.append(chr((ord(ch) - base + 13) % 26 + base))
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._leet_dec:
                result.append(self._leet_dec[ch])
            elif ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr((ord(ch) - base + 13) % 26 + base))
            else:
                result.append(ch)
        return ''.join(result)
