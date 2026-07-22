class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            loop through the array
            if a number isn't bigger than the top of the stack add it
            if it is pop until it isn't and keep track of the amount popped
            then use the popped to find the index of which index to update
        '''

        stack = []
        res = [0] * len(temperatures)
        '''
        [1,0,1,0,0,0,0]
        [38,36,35]
        count = 1
        i = 5
        '''
        for i,t in enumerate(temperatures):
            top = temperatures[stack[-1]] if stack else float('inf')
            while t > top and stack:
                index = stack.pop()
                res[index] = i - index
                top = temperatures[stack[-1]] if stack else float('inf')
            stack.append(i)
        return res
            
