class AlternatingCaseAndReverseCipher:
    def __init__(self):
        pass

    def _alternate_case(self, text: str) -> str:
        result = []
        alpha_count = 0
        for ch in text:
            if ch.isalpha():
                alpha_count += 1
                if alpha_count % 2 == 1:
                    result.append(ch.upper())
                else:
                    result.append(ch.lower())
            else:
                result.append(ch)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._alternate_case(plaintext[::-1])

    def decrypt(self, ciphertext: str) -> str:
        return self._alternate_case(ciphertext)[::-1]
