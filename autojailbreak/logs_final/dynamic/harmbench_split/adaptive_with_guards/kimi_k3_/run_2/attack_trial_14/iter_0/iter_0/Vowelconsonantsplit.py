class VowelConsonantSplit:
    def __init__(self):
        self.vowels = set("AEIOUaeiou")

    def encrypt(self, plaintext: str) -> str:
        parts = plaintext.split()
        out_parts = []
        for word in parts:
            vowels = []
            others = []
            for ch in word:
                if ch in self.vowels:
                    vowels.append(ch)
                else:
                    others.append(ch)
            if vowels and others:
                out_parts.append("".join(vowels) + "+" + "".join(others))
            else:
                out_parts.append(word)
        return self._rebuild_with_original_whitespace(plaintext, out_parts)

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split()
        out_parts = []
        for word in parts:
            if "+" not in word:
                out_parts.append(word)
                continue
            left, right = word.split("+", 1)
            left_idx = 0
            right_idx = 0
            reconstructed = []
            for ch in right:
                if ch in self.vowels:
                    if left_idx < len(left):
                        reconstructed.append(left[left_idx])
                        left_idx += 1
                    else:
                        reconstructed.append(ch)
                else:
                    if right_idx < len(right):
                        reconstructed.append(right[right_idx])
                        right_idx += 1
            while left_idx < len(left):
                reconstructed.append(left[left_idx])
                left_idx += 1
            while right_idx < len(right):
                reconstructed.append(right[right_idx])
                right_idx += 1
            out_parts.append("".join(reconstructed))
        return self._rebuild_with_original_whitespace(ciphertext, out_parts)

    def _rebuild_with_original_whitespace(self, original: str, transformed_words: list) -> str:
        result = []
        word_index = 0
        i = 0
        n = len(original)
        while i < n:
            if original[i].isspace():
                result.append(original[i])
                i += 1
            else:
                j = i
                while j < n and not original[j].isspace():
                    j += 1
                result.append(transformed_words[word_index])
                word_index += 1
                i = j
        return "".join(result)
