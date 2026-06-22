class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return True -> if anagram
        # Return False -> NOT anagram
        # Anagram = word with same characters -> ordered differently

        # Check the lengths
        if len(s) != len(t):
            return False

        # Count the frequencies of characters
        frequencies = {}

        # Loop through s:
        for char in s:
            frequencies[char] = frequencies.get(char, 0) + 1
        
        # Loop through t and decrement:
        for char in t:
            frequencies[char] = frequencies.get(char, 0) - 1

        # Check the counts: (Should all be 0's if anagram)
        for count in frequencies.values():
            if count != 0:
                return False
        
        return True