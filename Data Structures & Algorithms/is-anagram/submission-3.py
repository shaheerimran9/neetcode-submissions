class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Input ->  two strings s & t
        #Output -> True if anagram / False if not anagram
        #Anagram -> Word with exact same characters rearranged

        #1. Check length -> If not same length can't be anagrams
        if len(s) != len(t):
            return False

        #2. Add string characters to hashmap
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        #3. Compare the counts of the chars in both hashmaps
        for char in s:
            if s_count[char] != t_count.get(char):
                return False
        return True
