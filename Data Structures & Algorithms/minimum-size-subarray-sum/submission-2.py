class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums)

        sum = 0
        l = 0
        r = 0
        while r < len(nums):
            sum += nums[r]
            if sum >= target:
                while sum - nums[l] >= target:
                    sum -= nums[l] # = 12 11
                    l += 1 # = 1 2
                result = min( r - l + 1, result ) # = 3
                print("result",result)
            r += 1

        if l == 0 and sum < target:
            return 0
        return result