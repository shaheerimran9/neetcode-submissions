class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Input -> Two strings s & t
        #Output -> True if s & t are anagrams || False if not anagrams

        #s & t are anagrams if they have the exact same characters
        #s & t must have the same exact *frequencies* of characters

        # if s & t are different lengths -> Not anagrams -> False

        # Use a hashmap to map character -> frequency
        # Loop through s first and update the freqencies in hashmap
        # Loop through t and decrement the frequencies in hashmap
        # Loop through the values in hashmap
        # If any value != 0 return False
        # Return True at the end

        if len(s) != len(t):
            return False

        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
        for char in t:
            freq_map[char] -= 1
        for freq in freq_map.values():
            if freq != 0:
                return False
        return True

