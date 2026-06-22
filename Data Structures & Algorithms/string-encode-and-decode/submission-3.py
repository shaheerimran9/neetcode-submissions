class Solution:

    def encode(self, strs: List[str]) -> str:
        # Input -> List of strings
        # Output -> One single string
        # 5#Hello#World
        
        # Initialize res
        # Loop through each word
            # Append to res: len(word) STRING!, delimiter, and word
        # Return res
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        # Input - String
        # Output -> Array of words from the string

        # Initialize res -> []
        # Use two pointers i and j && loop through while i < len(word)
            # i will point at the len, j will grab the word
            # set j = i
            # increment j until we get to our delimiter '#'
            # i:j is the len of our word -> CONVERT TO INT
            # word will be j (at delimiter) + 1 (start of word) + len
            # append the word to our res array
            # set i = j + 1 + len (because that is the start of next word exclusive)
        # Return res

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_len = int(s[i:j])
            word = s[j + 1: j + 1 + word_len]
            res.append(word)
            i = j + 1 + word_len
        return res