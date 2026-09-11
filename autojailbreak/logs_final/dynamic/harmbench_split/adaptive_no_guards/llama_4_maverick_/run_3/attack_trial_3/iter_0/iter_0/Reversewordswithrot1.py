class ReverseWordsWithRot1:
    def __init__(self):
        pass

    def _shift_char(self, ch: str, delta: int) -> str:
        if 'a' <= ch <= 'z':
            return chr((ord(ch) - ord('a') + delta) % 26 + ord('a'))
        if 'A' <= ch <= 'Z':
            return chr((ord(ch) - ord('A') + delta) % 26 + ord('A'))
        return ch

    def _transform_word_encrypt(self, word: str) -> str:
        reversed_word = word[::-1]
        return ''.join(self._shift_char(ch, 1) for ch in reversed_word)

    def _transform_word_decrypt(self, word: str) -> str:
        shifted_back = ''.join(self._shift_char(ch, -1) for ch in word)
        return shifted_back[::-1]

    def encrypt(self, plaintext: str) -> str:
        result = []
        word = []
        for ch in plaintext:
            if ch.isalpha():
                word.append(ch)
            else:
                if word:
                    result.append(self._transform_word_encrypt(''.join(word)))
                    word = []
                result.append(ch)
        if word:
            result.append(self._transform_word_encrypt(''.join(word)))
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        word = []
        for ch in ciphertext:
            if ch.isalpha():
                word.append(ch)
            else:
                if word:
                    result.append(self._transform_word_decrypt(''.join(word)))
                    word = []
                result.append(ch)
        if word:
            result.append(self._transform_word_decrypt(''.join(word)))
        return ''.join(result)
