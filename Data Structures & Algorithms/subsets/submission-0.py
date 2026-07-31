class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curSet = []
        def backtrack(i):
            nonlocal res
            if i >= len(nums):
                res.append(curSet[:])
                return
            curSet.append(nums[i])
            backtrack(i+1)
            curSet.pop()
            backtrack(i+1)

        backtrack(0)
        return res
            
