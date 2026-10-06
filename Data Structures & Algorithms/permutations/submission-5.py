class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        used = [False] * len(nums)

        def dfs(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            for x in range(len(nums)):
                if used[x]:
                    continue
                curr.append(nums[x])
                used[x] = True
                dfs(i + 1)
                curr.pop()
                used[x] = False

        dfs(0)
        return res