class LeetSpeakBasicSubstitution:
    def __init__(self):
        self.enc = {
            "e": "3",
            "E": "3",
            "t": "7",
            "T": "7",
            "a": "4",
            "A": "4",
            "o": "0",
            "O": "0",
            "i": "1",
            "I": "1",
        }
        self.dec = {
            "3": "e",
            "7": "t",
            "4": "a",
            "0": "o",
            "1": "i",
        }

    def encrypt(self, plaintext: str) -> str:
        return "".join(self.enc.get(ch, ch) for ch in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return "".join(self.dec.get(ch, ch) for ch in ciphertext)
