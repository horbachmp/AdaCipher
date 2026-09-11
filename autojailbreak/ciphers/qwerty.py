class QwertyCipher:
    def __init__(self):
        self.plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.cipher_alphabet = "qwertyuiopasdfghjklzxcvbnm"

        self.encrypt_map = {
            p: c for p, c in zip(self.plain_alphabet, self.cipher_alphabet)
        }
        self.decrypt_map = {
            c: p for p, c in zip(self.plain_alphabet, self.cipher_alphabet)
        }

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    if char not in self.encrypt_map:
                        ciphertext += char
                    else:
                        ciphertext += self.encrypt_map[char]
                else:
                    if char.lower() not in self.encrypt_map:
                        ciphertext += char
                    else:
                        ciphertext += self.encrypt_map[char.lower()].upper()
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    if char not in self.decrypt_map:
                        plaintext += char
                    else:
                        plaintext += self.decrypt_map[char]
                else:
                    if char.lower() not in self.decrypt_map:
                        plaintext += char
                    else:
                        plaintext += self.decrypt_map[char.lower()].upper()
            else:
                plaintext += char
        return plaintext
