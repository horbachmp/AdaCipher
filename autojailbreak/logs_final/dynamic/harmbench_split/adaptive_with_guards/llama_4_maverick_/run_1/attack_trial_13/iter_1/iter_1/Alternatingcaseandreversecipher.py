class AlternatingCaseAndReverseCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        reversed_text = plaintext[::-1]
        result = []
        alpha_count = 0
        for char in reversed_text:
            if char.isalpha():
                alpha_count += 1
                result.append(char.upper() if alpha_count % 2 == 1 else char.lower())
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        alternated = []
        alpha_count = 0
        for char in ciphertext:
            if char.isalpha():
                alpha_count += 1
                alternated.append(char.upper() if alpha_count % 2 == 1 else char.lower())
            else:
                alternated.append(char)
        return "".join(alternated)[::-1]
