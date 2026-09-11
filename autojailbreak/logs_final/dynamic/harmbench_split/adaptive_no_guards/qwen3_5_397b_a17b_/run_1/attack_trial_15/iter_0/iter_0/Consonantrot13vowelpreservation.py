class ConsonantRot13VowelPreservation:
    def __init__(self):
        self._lower = "bcdfghjklmnpqrstvwxyz"
        self._upper = self._lower.upper()
        self._lower_map = {c: self._lower[(i + 13) % len(self._lower)] for i, c in enumerate(self._lower)}
        self._upper_map = {c: self._upper[(i + 13) % len(self._upper)] for i, c in enumerate(self._upper)}
        self._vowels = set("aeiouAEIOU")

    def encrypt(self, plaintext: str) -> str:
        out = []
        for ch in plaintext:
            if ch in self._vowels or not ch.isalpha():
                out.append(ch)
            elif ch.islower():
                out.append(self._lower_map.get(ch, ch))
            else:
                out.append(self._upper_map.get(ch, ch))
        return "".join(out)

    def decrypt(self, ciphertext: str) -> str:
        out = []
        for ch in ciphertext:
            if ch in self._vowels or not ch.isalpha():
                out.append(ch)
            elif ch.islower():
                out.append(self._lower_map.get(ch, ch))
            else:
                out.append(self._upper_map.get(ch, ch))
        return "".join(out)
