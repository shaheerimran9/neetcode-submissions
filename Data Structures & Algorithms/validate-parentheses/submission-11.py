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

        for p in s:
            if p not in char_map:
                stack.append(p)
            else:
                if stack and char_map[p] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack
