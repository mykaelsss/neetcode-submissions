class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            top = temperatures[stack[-1]] if stack else float('inf')
            while t > top and stack:
                index = stack.pop()
                res[index] = i - index
                top = temperatures[stack[-1]] if stack else float('inf')
            stack.append(i)
        return res
            
