class VowelConsonantSplitCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        result = []
        vowels = set("AEIOUaeiou")
        for token in plaintext.split(" "):
            if token.isalpha():
                consonants = []
                vowel_chars = []
                for ch in token:
                    if ch in vowels:
                        vowel_chars.append(ch)
                    else:
                        consonants.append(ch)
                result.append("".join(consonants + vowel_chars))
            else:
                if any(ch.isalpha() for ch in token):
                    chars = []
                    consonants = []
                    vowel_chars = []
                    for ch in token:
                        if ch.isalpha():
                            if ch in vowels:
                                vowel_chars.append(ch)
                            else:
                                consonants.append(ch)
                        else:
                            if consonants or vowel_chars:
                                chars.append("".join(consonants + vowel_chars))
                                consonants = []
                                vowel_chars = []
                            chars.append(ch)
                    if consonants or vowel_chars:
                        chars.append("".join(consonants + vowel_chars))
                    result.append("".join(chars))
                else:
                    result.append(token)
        return " ".join(result)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext
