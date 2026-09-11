class ConsonantVowelInterleaveCipher:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def _is_letter(self, ch: str) -> bool:
        return ch.isalpha()

    def _is_vowel(self, ch: str) -> bool:
        return ch in self.vowels

    def _transform_word_encrypt(self, word: str) -> str:
        consonants = [ch for ch in word if self._is_letter(ch) and not self._is_vowel(ch)]
        vowels = [ch for ch in word if self._is_vowel(ch)]
        result = []
        i = j = 0
        while i < len(consonants) or j < len(vowels):
            if i < len(consonants):
                result.append(consonants[i])
                i += 1
            if j < len(vowels):
                result.append(vowels[j])
                j += 1
        return "".join(result)

    def _transform_word_decrypt(self, word: str) -> str:
        consonants = []
        vowels = []
        for idx, ch in enumerate(word):
            if idx % 2 == 0:
                consonants.append(ch)
            else:
                vowels.append(ch)
        result = []
        i = j = 0
        total = len(word)
        c_remaining = len(consonants)
        v_remaining = len(vowels)
        for idx in range(total):
            if idx % 2 == 0:
                if c_remaining > 0:
                    result.append(consonants[i])
                    i += 1
                    c_remaining -= 1
                else:
                    result.append(vowels[j])
                    j += 1
                    v_remaining -= 1
            else:
                if v_remaining > 0:
                    result.append(vowels[j])
                    j += 1
                    v_remaining -= 1
                else:
                    result.append(consonants[i])
                    i += 1
                    c_remaining -= 1
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        parts = []
        current = []
        for ch in plaintext:
            if self._is_letter(ch):
                current.append(ch)
            else:
                if current:
                    parts.append(self._transform_word_encrypt("".join(current)))
                    current = []
                parts.append(ch)
        if current:
            parts.append(self._transform_word_encrypt("".join(current)))
        return "".join(parts)

    def decrypt(self, ciphertext: str) -> str:
        parts = []
        current = []
        for ch in ciphertext:
            if self._is_letter(ch):
                current.append(ch)
            else:
                if current:
                    parts.append(self._transform_word_decrypt("".join(current)))
                    current = []
                parts.append(ch)
        if current:
            parts.append(self._transform_word_decrypt("".join(current)))
        return "".join(parts)
