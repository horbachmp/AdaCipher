class ConsonantVowelInterleaveCipher:
    def __init__(self):
        self._enc_lower_vowels = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
        self._dec_lower_vowels = {'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o'}
        self._enc_upper_vowels = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
        self._dec_upper_vowels = {'A': 'U', 'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O'}

        lower_consonants = "bcdfghjklmnpqrstvwxyz"
        upper_consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        self._enc_lower_consonants = {lower_consonants[i]: lower_consonants[(i + 1) % len(lower_consonants)] for i in range(len(lower_consonants))}
        self._dec_lower_consonants = {lower_consonants[i]: lower_consonants[(i - 1) % len(lower_consonants)] for i in range(len(lower_consonants))}
        self._enc_upper_consonants = {upper_consonants[i]: upper_consonants[(i + 1) % len(upper_consonants)] for i in range(len(upper_consonants))}
        self._dec_upper_consonants = {upper_consonants[i]: upper_consonants[(i - 1) % len(upper_consonants)] for i in range(len(upper_consonants))}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self._enc_lower_vowels:
                result.append(self._enc_lower_vowels[ch])
            elif ch in self._enc_upper_vowels:
                result.append(self._enc_upper_vowels[ch])
            elif ch in self._enc_lower_consonants:
                result.append(self._enc_lower_consonants[ch])
            elif ch in self._enc_upper_consonants:
                result.append(self._enc_upper_consonants[ch])
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self._dec_lower_vowels:
                result.append(self._dec_lower_vowels[ch])
            elif ch in self._dec_upper_vowels:
                result.append(self._dec_upper_vowels[ch])
            elif ch in self._dec_lower_consonants:
                result.append(self._dec_lower_consonants[ch])
            elif ch in self._dec_upper_consonants:
                result.append(self._dec_upper_consonants[ch])
            else:
                result.append(ch)
        return "".join(result)
