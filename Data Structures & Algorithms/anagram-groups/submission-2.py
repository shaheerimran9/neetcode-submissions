class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input -> array of strings strs
        # Output -> array of sublists of anagrams AKA [ [], [], ]

        # Anagram -> string with EXACT same characters as another
        # Two strs are anagram if their character frequencies are SAME

        # Initialize result array
        # Initialize a hashmap { signature: [strs] }
        # Loop through the strs
            # Create a signature for each string
            # Use the signature as a key in the hashmap -> add str to it
        # Loop through the values in hashmap
            # Append each value to the result array
        # Return res

        res = []
        groups = defaultdict(list)

        for s in strs:
            signature = [0] * 26
            for i in range(len(s)):
                index = ord(s[i]) - ord('a')
                signature[index] += 1
            groups[tuple(signature)].append(s)
            
        return list(groups.values())