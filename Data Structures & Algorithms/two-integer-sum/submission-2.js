class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();

        for (let i = 0; i < nums.length; i++) {
            const potential = target - nums[i]
            if (map.has(potential)) return [map.get(potential), i]
            map.set(nums[i], i)
        }
    }
}
