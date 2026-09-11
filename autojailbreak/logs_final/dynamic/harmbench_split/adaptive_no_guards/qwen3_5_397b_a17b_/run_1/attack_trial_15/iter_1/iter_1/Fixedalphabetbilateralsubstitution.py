class FixedAlphabetBilateralSubstitution:
    def __init__(self):
        lower_vowels = set("aeiou")
        lower_consonants = "bcdfghjklmnpqrstvwxyz"
        self._map = {}
        for a, b in zip(lower_consonants, reversed(lower_consonants)):
            self._map[a] = b
            self._map[b] = a
        upper_consonants = lower_consonants.upper()
        for a, b in zip(upper_consonants, reversed(upper_consonants)):
            self._map[a] = b
            self._map[b] = a
        for v in lower_vowels:
            self._map[v] = v
        for v in "AEIOU":
            self._map[v] = v

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._map.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._map.get(ch, ch) for ch in ciphertext)
