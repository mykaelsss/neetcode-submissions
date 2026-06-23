class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        values_list = sorted(list(freq.items()), key=lambda freq: freq[1], reverse=True)

        print(values_list)
        
        res = []

        for i in range(len(values_list)):
            if i == k:
                break
            res.append(values_list[i][0])
        
        return res
        
        
            
         