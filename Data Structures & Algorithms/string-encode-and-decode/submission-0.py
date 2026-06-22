class Solution:

    def encode(self, strs: List[str]) -> str:
        # Get the length of the world
        # Use a delimiter
        # Join the string together -> 5#Hello
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s))+'#'+s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        output = []
        # Start a pointer with the number
        i = 0
        while i < len(s):
            j = i
            # Increment a second pointer till the # to get word length
            while s[j] != '#':
                j += 1
            word_len = int(s[i:j])            
            # Grab the word up until the word_len
            word = s[j+1:j+1+word_len]
            # Append word to output
            output.append(word)
            i = j + 1 + word_len
        return output
