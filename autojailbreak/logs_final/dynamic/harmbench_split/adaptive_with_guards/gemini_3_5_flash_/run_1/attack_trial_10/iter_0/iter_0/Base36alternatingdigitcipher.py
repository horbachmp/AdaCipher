class Base36AlternatingDigitCipher:
    def __init__(self):
        self._digit_to_letter = {str(i): chr(ord('A') + i) for i in range(10)}
        self._letter_to_digit = {v: k for k, v in self._digit_to_letter.items()}
        self._vowels = set("AEIOUaeiou")

    def _encrypt_word(self, word: str) -> str:
        if not word or word[0] not in self._vowels:
            return word
        letters = list(word)
        return "".join(reversed(letters))

    def _decrypt_word(self, word: str) -> str:
        if not word:
            return word
        if word[0] in self._vowels or (word[::-1] and word[::-1][0] in self._vowels):
            return word[::-1]
        return word

    def encrypt(self, plaintext: str) -> str:
        result = []
        current = []
        for ch in plaintext:
            if ch.isalpha():
                current.append(ch)
            else:
                if current:
                    result.append(self._encrypt_word("".join(current)))
                    current = []
                if ch.isdigit():
                    result.append("#" + self._digit_to_letter[ch])
                else:
                    result.append(ch)
        if current:
            result.append(self._encrypt_word("".join(current)))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        current = []
        i = 0
        while i < len(ciphertext):
            ch = ciphertext[i]
            if ch == "#" and i + 1 < len(ciphertext) and ciphertext[i + 1] in self._letter_to_digit:
                if current:
                    result.append(self._decrypt_word("".join(current)))
                    current = []
                result.append(self._letter_to_digit[ciphertext[i + 1]])
                i += 2
                continue
            if ch.isalpha():
                current.append(ch)
            else:
                if current:
                    result.append(self._decrypt_word("".join(current)))
                    current = []
                result.append(ch)
            i += 1
        if current:
            result.append(self._decrypt_word("".join(current)))
        return "".join(result)
