class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        totalSum = 0
        for op in operations:
            if op not in {'+', 'D', 'C'}:
                stack.append(int(op))
            elif op == '+':
                newScore = stack[-1] + stack[-2]
                stack.append(newScore)
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
        for score in stack:
            totalSum += score
        return totalSum
