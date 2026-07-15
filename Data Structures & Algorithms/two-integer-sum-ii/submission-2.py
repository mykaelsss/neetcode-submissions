class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            num1, num2 = numbers[l], numbers[r]
            currSum = num1 + num2

            if currSum == target:
                return [l + 1, r + 1]
            elif currSum > target:
                r -= 1
            else:
                l += 1
        
