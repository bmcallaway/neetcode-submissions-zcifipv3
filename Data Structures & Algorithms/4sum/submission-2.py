class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0

        while i < len(nums) - 3:
            x = i + 1
            while x < len(nums) - 2:
                l = x + 1
                r = len(nums) - 1
                while l < r:
                    val = nums[i] + nums[x] + nums[l] + nums[r]
                    if val > target:
                        r -= 1
                    elif val < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[x], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < len(nums) and nums[l] == nums[l-1]:
                            l +=1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                x += 1
                while x < len(nums) - 2 and nums[x] == nums[x-1]:
                    x += 1
            i += 1
            while i < len(nums) -3 and nums[i] == nums[i-1]:
                i +=1        

        return res