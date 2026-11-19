class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(pos):
            if pos >= len(nums):
                res.append(curr[:])
                return
            curr.append(nums[pos])
            dfs(pos + 1)
            curr.pop()
            dfs(pos + 1)

        dfs(0)

        return res
        