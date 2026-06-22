class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # j resets to i each time which means they're both at num
            j = i
            while s[j] != '#':
                j += 1
            # Need to get the word len
            # We do that by finding the '#' and everything before that is num
            # Get the word -> '#' + 1 till '#' + 1 + word_len
            word_len = int(s[i:j])
            res.append(s[j+1:j+1+word_len])
            # moving i to the next number in the string
            i = j + 1 + word_len
        return res