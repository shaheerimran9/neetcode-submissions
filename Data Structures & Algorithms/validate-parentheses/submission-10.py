class Solution:
    def isValid(self, s: str) -> bool:
        #Input -> String s consisting of (), {}, [] characters
        #Output -> Return true is s is valid || False if not valid
        
        char_map = {
            ']': '[',
            '}': '{',
            ')' : '('
        }

        stack = []

        for char in s:
            #Opening char
            if char not in char_map:
                stack.append(char)
            else:
                #Closing bracket
                if stack and stack[-1] == char_map[char]:
                    stack.pop()
                else:
                    return False
        return not stack