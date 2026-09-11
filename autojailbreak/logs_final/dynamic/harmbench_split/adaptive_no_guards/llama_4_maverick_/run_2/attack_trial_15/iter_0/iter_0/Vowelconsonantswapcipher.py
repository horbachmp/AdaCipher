class VowelConsonantSwapCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def _is_letter(self, ch: str) -> bool:
        return ch.isalpha()

    def _is_vowel(self, ch: str) -> bool:
        return ch in self.vowels

    def _process_word_encrypt(self, word: str) -> str:
        chars = list(word)
        i = 0
        while i < len(chars) - 1:
            if self._is_letter(chars[i]) and self._is_letter(chars[i + 1]):
                if self._is_vowel(chars[i]) and not self._is_vowel(chars[i + 1]):
                    chars[i], chars[i + 1] = chars[i + 1], chars[i]
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        return "".join(chars)

    def _process_word_decrypt(self, word: str) -> str:
        chars = list(word)
        i = 0
        while i < len(chars) - 1:
            if self._is_letter(chars[i]) and self._is_letter(chars[i + 1]):
                if not self._is_vowel(chars[i]) and self._is_vowel(chars[i + 1]):
                    chars[i], chars[i + 1] = chars[i + 1], chars[i]
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        return "".join(chars)

    def encrypt(self, plaintext: str) -> str:
        result = []
        current = []
        for ch in plaintext:
            if ch.isalpha():
                current.append(ch)
            else:
                if current:
                    result.append(self._process_word_encrypt("".join(current)))
                    current = []
                result.append(ch)
        if current:
            result.append(self._process_word_encrypt("".join(current)))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        current = []
        for ch in ciphertext:
            if ch.isalpha():
                current.append(ch)
            else:
                if current:
                    result.append(self._process_word_decrypt("".join(current)))
                    current = []
                result.append(ch)
        if current:
            result.append(self._process_word_decrypt("".join(current)))
        return "".join(result)
