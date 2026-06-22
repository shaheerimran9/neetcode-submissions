class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Input -> Array of strings: tokens
        # Output -> Integer that is evaluation of the given expression

        # Use a stack
        # Loop through the tokens
        # If we see a number add it to the stack
        # If we see an operand:
            # Remove the last two numbers in the stack
            # Do the operation
            # Add the result back onto the stack
        # Return top of stack for the result

        stack = []
        for t in tokens:
            if t != '+' and t != '-' and t != '*' and t != '/':
                stack.append(int(t))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(num1 + num2)
                elif t == '-':
                    stack.append(num1 - num2)
                elif t == '*':
                    stack.append(num1 * num2)
                elif t == '/':
                    stack.append(int(num1 / num2))
        return stack[-1]