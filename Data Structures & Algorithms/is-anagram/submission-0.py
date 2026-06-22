class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFrequencies = {}
        tFrequencies = {}

        for char in s:
            if char in sFrequencies:
                sFrequencies[char] += 1
            else:
                sFrequencies[char] = 1
        
        for char in t:
            if char in tFrequencies:
                tFrequencies[char] +=1
            else:
                tFrequencies[char] = 1
        
        #Compare
        if sFrequencies != tFrequencies:
            return False
        return True
