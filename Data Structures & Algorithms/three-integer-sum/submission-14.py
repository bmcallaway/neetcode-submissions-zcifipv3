class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #-4 -1 -1 0 1 2
        # i  l        r t=-3
        # i     l     r
        # i       l   r t=-2
        # i         l r t=-1
        #    i  l     r t=0

        #0 0 0 0
        #i l   r t = 0
        nums.sort()
        result = []
        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total > 0:
                    r -= 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
                elif total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1

            
        return result