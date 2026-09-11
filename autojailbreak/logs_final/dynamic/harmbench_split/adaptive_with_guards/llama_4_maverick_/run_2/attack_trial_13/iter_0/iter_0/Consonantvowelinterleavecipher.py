class ConsonantVowelInterleaveCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        vowels = []
        consonants = []
        for ch in plaintext:
            if ch.isalpha():
                if ch.lower() in "aeiou":
                    vowels.append(ch)
                else:
                    consonants.append(ch)
        letters = consonants + vowels
        result = []
        idx = 0
        for ch in plaintext:
            if ch.isalpha():
                result.append(letters[idx])
                idx += 1
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext
