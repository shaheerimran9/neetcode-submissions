class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res, l = 0, 0
        for r in range(len(s)):
            length = (r - l) + 1
            #Update the count at s[r]
            count[s[r]] = 1 + count.get(s[r], 0)
            #Make sure window is valid
            while length - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                length = (r - l) + 1
            #Update res with max window length
            res = max(length, res)
        return res