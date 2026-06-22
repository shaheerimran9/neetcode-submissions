class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []

        # Adding numbers
        # Op on prev 2 numbers
        for token in tokens:
            # token is a number
            if token not in ops:
                stack.append(int(token))
            # token is not a number -> operand
            else:
                # pop last 2 numbers
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1+num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                # TRUNCATE to 0 -> Using / & int so there's no decimal
                elif token == '/':
                    stack.append(int(num1 / num2))
        return stack[-1]
            