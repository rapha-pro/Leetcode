class Solution:

    def encode(self, strs: List[str]) -> str:
        encryption = ""
        for s in strs:
            encryption += (str(len(s)) + "#" + s)
        return encryption

    def decode(self, s: str) -> List[str]:
        decryption, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_of_next_word = int(s[i:j])
            decryption.append(s[j + 1: j + 1 + length_of_next_word])
            i = j + 1 + length_of_next_word

        return decryption
