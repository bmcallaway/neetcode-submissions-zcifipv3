class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        x = 0
        while x < len(nums) - 2:
            l = x + 1
            r = len(nums) - 1  
            while l < r:
                total = nums[x] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                elif total == 0:
                    res.append([nums[x], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            x += 1
            while  x < len(nums) - 2 and nums[x] == nums[x-1]:
                x += 1

        # -1 -1 0 1
        return res
                