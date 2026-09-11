class VowelConsonantInterchangeCipher:
    def __init__(self):
        self._vowel_encrypt = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
        self._vowel_decrypt = {v: k for k, v in self._vowel_encrypt.items()}
        consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self._consonant_encrypt = {consonants[i]: consonants[(i + 1) % len(consonants)] for i in range(len(consonants))}
        self._consonant_decrypt = {v: k for k, v in self._consonant_encrypt.items()}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            upper = ch.upper()
            if upper in self._vowel_encrypt:
                mapped = self._vowel_encrypt[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            elif upper.isalpha():
                mapped = self._consonant_encrypt[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            upper = ch.upper()
            if upper in self._vowel_decrypt:
                mapped = self._vowel_decrypt[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            elif upper.isalpha():
                mapped = self._consonant_decrypt[upper]
                result.append(mapped if ch.isupper() else mapped.lower())
            else:
                result.append(ch)
        return ''.join(result)
