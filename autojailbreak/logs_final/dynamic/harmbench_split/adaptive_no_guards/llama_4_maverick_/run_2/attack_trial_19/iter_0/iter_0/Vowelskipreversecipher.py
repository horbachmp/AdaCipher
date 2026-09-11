class VowelSkipReverseCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def _transform_word(self, word: str) -> str:
        consonants = [ch for ch in word if ch.isalpha() and ch not in self.vowels]
        consonants.reverse()
        result = []
        idx = 0
        for ch in word:
            if ch.isalpha() and ch not in self.vowels:
                new_ch = consonants[idx]
                if ch.isupper():
                    new_ch = new_ch.upper()
                else:
                    new_ch = new_ch.lower()
                result.append(new_ch)
                idx += 1
            else:
                result.append(ch)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return "".join(self._transform_word(word) for word in plaintext.split(" ")) if plaintext else ""

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self._transform_word(word) for word in ciphertext.split(" ")) if ciphertext else ""
