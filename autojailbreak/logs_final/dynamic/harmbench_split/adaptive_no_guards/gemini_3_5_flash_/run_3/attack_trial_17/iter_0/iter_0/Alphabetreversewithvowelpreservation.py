class AlphabetReverseWithVowelPreservation:
    def __init__(self):
        self.upper_vowels = set("AEIOU")
        self.lower_vowels = set("aeiou")
        upper_consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        lower_consonants = "bcdfghjklmnpqrstvwxyz"
        reversed_upper = "ZYXWVTSRQP NMLKJHGFDCB".replace(" ", "")
        reversed_lower = "zyxwvtsrqpnmlkjhgf dcb".replace(" ", "")
        self.enc_map = {}
        self.dec_map = {}
        for a, b in zip(upper_consonants, reversed_upper):
            self.enc_map[a] = b
            self.dec_map[b] = a
        for a, b in zip(lower_consonants, reversed_lower):
            self.enc_map[a] = b
            self.dec_map[b] = a

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.upper_vowels or ch in self.lower_vowels or not ch.isalpha():
                result.append(ch)
            else:
                result.append(self.enc_map.get(ch, ch))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.upper_vowels or ch in self.lower_vowels or not ch.isalpha():
                result.append(ch)
            else:
                result.append(self.dec_map.get(ch, ch))
        return "".join(result)
