class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in '+*-/':
                stack.append(int(t))
            elif t == '+':
                num_2, num_1 = stack.pop(), stack.pop()
                stack.append(num_1 + num_2)
            elif t == '*':
                num_2, num_1 = stack.pop(), stack.pop()
                stack.append(num_1 * num_2)
            elif t == '-':
                num_2, num_1 = stack.pop(), stack.pop()
                stack.append(num_1 - num_2)
            elif t == '/':
                num_2, num_1 = stack.pop(), stack.pop()
                stack.append(int(num_1 / num_2))
        return stack[-1]