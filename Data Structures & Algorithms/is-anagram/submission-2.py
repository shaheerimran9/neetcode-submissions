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
        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1
        
        #3. Compare the counts of the chars in both hashmaps
        for char in s:
            if s_count[char] != t_count.get(char):
                return False
        return True
