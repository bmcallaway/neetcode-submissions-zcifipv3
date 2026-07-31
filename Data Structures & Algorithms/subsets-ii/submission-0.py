class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curSet = []
        nums.sort()
        def dfs(i):
            nonlocal curSet, res
            if i >= len(nums):
                res.append(curSet[:])
                return
            curSet.append(nums[i])
            dfs(i+1)
            curSet.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            dfs(i)
        
        dfs(0)

        return res
            