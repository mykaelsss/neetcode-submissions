class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        seen = set()
        nums.sort()

        for i in range(n-2):
            l,r = i + 1, n - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                seq = sorted((nums[i], nums[l], nums[r]))
                seqStr = "".join(str(num) for num in seq)
                if currSum == 0 and seqStr not in seen:
                    res.append([nums[i],nums[l],nums[r]])
                    seen.add(seqStr)
                elif currSum > 0:
                    if nums[l] > nums[r]:
                        l = l + 1
                    else:
                        r = r - 1
                else:
                    if nums[l] > nums[r]:
                        r = r - 1
                    else:
                        l = l + 1
        
        return res
