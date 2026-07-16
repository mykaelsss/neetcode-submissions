class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxArea = 0

        while i < j:
            maxHeight = min(heights[i], heights[j])
            diff = j - i
            product = maxHeight * diff
            maxArea = max(product, maxArea)
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxArea