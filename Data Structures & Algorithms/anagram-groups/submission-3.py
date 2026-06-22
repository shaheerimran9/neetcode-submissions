class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Input -> array of strings -> strs
        #Output -> sublists of anagrams in any order
        #Note - Basically taking the strings and grouping the anagrams

        #Anagrams = exact same freq of chars
        # Main question -> How do we know which strs are anagrams
        # They have to have the same FREQ of chars

        # Approach 1:
        # We could sort all the strings -> same strs are anagrams
        # Use a hashmap with the sorted str as key -> map it to list of similar strs
        # Issue -> Have to sort so nlogn time complexity

        # Approach 2:
        # We want to avoid sorting BUT need a key for the hashmap
        # We could make a signature using the freq of chars as the key
        # Have a dict -> signature mapped to list of anagrams
        # Loop through each string
        # Create the signature -> [0,0,0,0] -> array with ord freq
        # Add the string to the anagram list in dict with signature
        # IMP NOTE -> lists can't be keys in python dict so use a tuple
        # Return all the values in the dict in the end

        anagrams = defaultdict(list) #signatures -> anagrams via lists

        for str in strs:
            signature = [0] * 26
            for char in str:
                signature[ord(char) - ord('a')] += 1
            anagrams[tuple(signature)].append(str)
        
        return list(anagrams.values())