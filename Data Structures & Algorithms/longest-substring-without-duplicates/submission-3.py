class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Input -> String s
        #Output -> Length of longest substring without duplicates

        #We can use two pointers and a set to track seen characters
        #Use two pointers at the start
        #Left pointer will be the start of the substring
        #Right pointer will be the end of the substring
        #If right pointer encounters a seen character
        #Then we remove from the left until the substring is valid
        #Track the length of the substring using r - l + 1

        l = 0
        max_length = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_length = max((r - l) + 1, max_length)
        return max_length