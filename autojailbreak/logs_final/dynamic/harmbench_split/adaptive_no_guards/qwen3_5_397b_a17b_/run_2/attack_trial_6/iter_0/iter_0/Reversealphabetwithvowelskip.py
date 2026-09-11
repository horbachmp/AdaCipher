class ReverseAlphabetWithVowelSkip:
    def __init__(self):
        self._consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self._reversed = self._consonants[::-1]
        self._enc_map_upper = {c: r for c, r in zip(self._consonants, self._reversed)}
        self._enc_map_lower = {c.lower(): r.lower() for c, r in zip(self._consonants, self._reversed)}

    def _transform(self, text: str) -> str:
        out = []
        vowels = set("AEIOUaeiou")
        for ch in text:
            if not ch.isalpha() or ch in vowels:
                out.append(ch)
            elif ch.isupper():
                out.append(self._enc_map_upper.get(ch, ch))
            else:
                out.append(self._enc_map_lower.get(ch, ch))
        return "".join(out)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext)
