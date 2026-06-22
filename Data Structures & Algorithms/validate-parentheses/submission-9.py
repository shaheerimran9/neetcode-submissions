class Solution:
    def isValid(self, s: str) -> bool:
        map= {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for p in s:
            #opening
            if p not in map:
                stack.append(p)
            else:
                if not stack or stack[-1] != map[p]:
                    return False
                stack.pop()
        return not stack
                
