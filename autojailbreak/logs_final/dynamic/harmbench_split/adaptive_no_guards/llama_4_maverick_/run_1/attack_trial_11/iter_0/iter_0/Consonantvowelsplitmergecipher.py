class ConsonantVowelSplitMergeCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        vowels = set("aeiouAEIOU")
        result = []
        current = []

        def flush(word):
            consonants = [ch for ch in word if ch.isalpha() and ch not in vowels]
            vowel_chars = [ch for ch in word if ch.isalpha() and ch in vowels]
            return "".join(consonants + vowel_chars)

        for ch in plaintext:
            if ch.isalpha():
                current.append(ch)
            else:
                if current:
                    result.append(flush(current))
                    current = []
                result.append(ch)
        if current:
            result.append(flush(current))
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext
