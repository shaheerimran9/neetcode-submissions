class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}': '{', ')': '(', ']': '['}
        for p in s:
            #Opening Parenthesis -> Just add to stack
            if p not in closeToOpen:
                stack.append(p)
            else:
                #Closing Parenthesis -> Check if matching
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
        return not stack