class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []
        def dfs(pos):
            nonlocal stack, res
            if pos >= len(nums):
                res.append(stack[:])
                return
            stack.append(nums[pos])
            dfs(pos+1)
            stack.pop()
            dfs(pos+1)
        dfs(0)
        return res
        #res = [1,2,3] [1,2] [1, 3] [1] [2, 3] [2]
            