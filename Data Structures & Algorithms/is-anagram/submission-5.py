class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return True -> if anagram
        # Return False -> NOT anagram
        # Anagram = word with same characters -> ordered differently

        # First -> check the lengths
        
        # Loop through first string
            # Create frequency hashmap {char : frequency}

        # Loop through second string
            # Decrement frequency at each char
        
        # Loop through the freq hashmap
            # If any val does not have freq 0 return False
        
        # Return true -> All val freq = 0 means same string

        if len(s) != len(t):
            return False
        
        freq_map = defaultdict(int) # char : freq
        for c in s:
            freq_map[c] += 1
        
        for c in t:
            freq_map[c] -= 1

        for freq in freq_map.values():
            if freq != 0:
                return False
        
        return True

