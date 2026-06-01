class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1


        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            m = math.floor((r+l) / 2)
            if nums[m] >= nums[l] and nums[m] >= nums[r]:
                l = m + 1
            elif nums[m] <= nums[l] and nums[m] <= nums[r]:
                r = m 

        return -1