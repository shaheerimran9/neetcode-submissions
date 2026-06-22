class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Input -> String s, int k
        #Output -> Return length of the longest substring with only one character

        #We're basically trying to find the longest substring that has only one
        #repeating character. We can replace up to k characters.

        #We can use a sliding window with two pointers
        #Left and Right start at the first character of s
        #Use a dict to track frequencies of characters
        #Check the length of the substring
        #It's valid if length - most freq char <= k

        l = 0
        max_length = 0
        max_freq = 0
        freq = defaultdict(int)

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(freq[s[r]], max_freq)
            while ((r - l) + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            max_length = max((r - l) + 1, max_length)
        return max_length