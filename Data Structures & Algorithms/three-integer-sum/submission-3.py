class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        seen = set()
        nums.sort()

        for i in range(n-2):
            j,k = i + 1, n - 1
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                seq = sorted((nums[i], nums[j], nums[k]))
                seqStr = "".join(str(num) for num in seq)
                if currSum == 0 and seqStr not in seen:
                    res.append([nums[i],nums[j],nums[k]])
                    seen.add(seqStr)
                elif currSum > 0:
                    if nums[j] > nums[k]:
                        j = j + 1
                    else:
                        k = k - 1
                else:
                    if nums[j] > nums[k]:
                        k = k - 1
                    else:
                        j = j + 1
        
        return res
