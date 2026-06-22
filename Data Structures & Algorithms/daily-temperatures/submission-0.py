class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # array ints -> temperatures
        # return -> array result with number of days for warmer temps

        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                pop_index = stack.pop()
                res[pop_index] = i - pop_index
            stack.append(i)
        return res