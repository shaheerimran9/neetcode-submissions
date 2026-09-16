class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = []
        for word in strs:
            new_str.append(str(len(word)) + "*" + word)
        return "".join(new_str)
    def decode(self, s: str) -> List[str]:
        output = []
        i = j = 0

        while i < len(s):
            while s[j] != "*":
                j += 1
            word_len = int(s[i:j])
            word = s[j + 1: j + 1 + word_len]
            output.append(word)

            i = j + 1 + word_len
            j = i

        return output



