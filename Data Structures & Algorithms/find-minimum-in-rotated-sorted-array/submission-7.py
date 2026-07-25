class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        #1 2 3 4 5 6
        #6 1 2 3 4 5
        #5 6 1 2 3 4
        #4 5 6 1 2 3
        #3 4 5 6 1 2
        #2 3 4 5 6 1
        while l <= r:
            m = math.floor((r+l)/2)
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else: return nums[m]

        return -1