class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2,20,4,10,3,4,5]
        {
            1: [1]
            2: [1,2,3]
            20: [20]
            4: [4,5]
            10: [10]
            3: [2,3,4]
            5: [5]
        }
        -create a dict 
        -loop through array and for each new number found add it to the dict
        -if the curr index - 1 exists in the dict then append the value of that key
        as the current numbers key: value and append the key itself to the back
        
        """

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        