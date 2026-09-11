class AtbashWithVowelShift:
    def __init__(self):
        self.vowel_encrypt = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A',
                              'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
        self.vowel_decrypt = {'A': 'U', 'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O',
                              'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o'}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch in self.vowel_encrypt:
                result.append(self.vowel_encrypt[ch])
            elif ch.isalpha():
                if ch.isupper():
                    result.append(chr(ord('Z') - (ord(ch) - ord('A'))))
                else:
                    result.append(chr(ord('z') - (ord(ch) - ord('a'))))
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch in self.vowel_decrypt:
                result.append(self.vowel_decrypt[ch])
            elif ch.isalpha():
                if ch.isupper():
                    result.append(chr(ord('Z') - (ord(ch) - ord('A'))))
                else:
                    result.append(chr(ord('z') - (ord(ch) - ord('a'))))
            else:
                result.append(ch)
        return ''.join(result)
