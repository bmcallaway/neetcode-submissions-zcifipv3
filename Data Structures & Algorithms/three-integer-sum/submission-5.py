class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        print(nums)
        while i < len(nums)-2:
            l = i + 1
            r = len(nums)-1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    print("i l r:",i,l,r)
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        return res
                    

