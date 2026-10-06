class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        currSum = 0

        def dfs(i):
            nonlocal currSum, res, curr
            if currSum >= target or i >= len(nums):
                if currSum == target:
                    res.append(curr[:])
                return
            curr.append(nums[i])
            currSum += nums[i]
            dfs(i)
            currSum -= nums[i]
            curr.pop()
            dfs(i + 1)

        dfs(0)
        return res
