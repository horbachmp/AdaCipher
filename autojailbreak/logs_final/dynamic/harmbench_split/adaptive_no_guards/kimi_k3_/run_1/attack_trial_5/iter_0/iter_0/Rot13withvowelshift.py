class Rot13WithVowelShift:
    def __init__(self):
        self._vowel_encrypt = {
            "A": "E", "E": "I", "I": "O", "O": "U", "U": "A",
            "a": "e", "e": "i", "i": "o", "o": "u", "u": "a",
        }
        self._vowel_decrypt = {v: k for k, v in self._vowel_encrypt.items()}
        consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
        shifted = ["N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M"]
        self._cons_encrypt_upper = {c: s for c, s in zip(consonants, shifted)}
        self._cons_decrypt_upper = {s: c for c, s in zip(consonants, shifted)}
        self._cons_encrypt_lower = {c.lower(): s.lower() for c, s in zip(consonants, shifted)}
        self._cons_decrypt_lower = {s.lower(): c.lower() for c, s in zip(consonants, shifted)}

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch in self._vowel_encrypt:
                out.append(self._vowel_encrypt[ch])
            elif ch in self._cons_encrypt_upper:
                out.append(self._cons_encrypt_upper[ch])
            elif ch in self._cons_encrypt_lower:
                out.append(self._cons_encrypt_lower[ch])
            else:
                out.append(ch)
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch in self._vowel_decrypt:
                out.append(self._vowel_decrypt[ch])
            elif ch in self._cons_decrypt_upper:
                out.append(self._cons_decrypt_upper[ch])
            elif ch in self._cons_decrypt_lower:
                out.append(self._cons_decrypt_lower[ch])
            else:
                out.append(ch)
        return "".join(out)
