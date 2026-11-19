class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        currSum = 0

        def dfs(pos):
            nonlocal currSum
            if pos >= len(nums) or currSum >= target:
                if currSum == target:
                    res.append(curr[:])
                return
            curr.append(nums[pos])
            currSum += nums[pos]
            dfs(pos)
            currSum -= curr.pop()
            dfs(pos + 1)

        dfs(0)
        return res