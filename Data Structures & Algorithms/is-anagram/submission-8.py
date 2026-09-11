class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Two strings = anagram if they have same characters
        # So we need to count number of characters in each string
        # If counts are same anagram
        # If counts not the same not anagram

        if len(s) != len(t):
            return False

        s_count = defaultdict(int)

        for char in s:
            s_count[char] += 1
        
        for char in t:
            s_count[char] -= 1


        for count in s_count.values():
            if count != 0:
                return False

        return True