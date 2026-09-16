class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Two strings = anagram if they have same characters
        # So we need to count number of characters in each string
        # If counts are same anagram
        # If counts not the same not anagram

        if len(s) != len(t):
            return False

        counts = defaultdict(int)

        for char in s:
            counts[char] += 1

        for char in t:
            counts[char] -= 1

        for count in counts.values():
            if count != 0:
                return False
        
        return True

