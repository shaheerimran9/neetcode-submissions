class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        res = []
        # 5#Hello3#Joe
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_len = int(s[i:j])
            word = s[j+1:j+1+word_len]
            res.append(word)
            i = j + 1 + word_len
        return res