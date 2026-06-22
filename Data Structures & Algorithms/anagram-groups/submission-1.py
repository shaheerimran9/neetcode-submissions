class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array -> strs
        # group all anagrams into sublists
        res = []
        groups = defaultdict(list)
        #1. Go through each word
        for s in strs:
            #2. Create a signature using ord
            signature = [0] * 26
            for char in s:
                signature[ord(char) - ord('a')] += 1
            #signature becomes key in hashmap
            #3. add normal word as value in hashmap
            groups[tuple(signature)].append(s)
        #5. return all the lists in the hashmap
        for l in groups.values():
            res.append(l)
        return res