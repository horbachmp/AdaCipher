class QwertyRot13HybridCipher:
    def __init__(self):
        self.qwerty = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.q_to_std = {q: s for s, q in enumerate(self.qwerty)}
        self.std_to_q = {s: q for s, q in enumerate(self.qwerty)}

    def encrypt(self, plaintext: str) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                is_lower = ch.islower()
                idx = ord(ch.upper()) - ord('A')
                q = self.qwerty[idx]
                rot_idx = (ord(q) - ord('A') + 13) % 26
                out = chr(rot_idx + ord('A'))
                if is_lower:
                    out = out.lower()
                result.append(out)
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext:
            if ch.isalpha():
                is_lower = ch.islower()
                rot_idx = (ord(ch.upper()) - ord('A') + 13) % 26
                q = chr(rot_idx + ord('A'))
                idx = self.q_to_std[q]
                out = chr(idx + ord('A'))
                if is_lower:
                    out = out.lower()
                result.append(out)
            else:
                result.append(ch)
        return "".join(result)
