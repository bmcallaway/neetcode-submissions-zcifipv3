class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = k - 1
        
        minAns = nums[r] - nums[l]

        while r+1 < len(nums):
            r += 1
            l += 1
            val = nums[r] - nums[l]
            minAns = min(val, minAns)
        return minAns