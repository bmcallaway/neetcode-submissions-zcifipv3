class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr, currSum = [], [], 0

        candidates.sort()
        def dfs(i):
            nonlocal currSum
            if i >= len(candidates) or currSum >= target:
                if currSum == target:
                    res.append(curr[:])
                return
            curr.append(candidates[i])
            currSum += candidates[i]
            dfs(i + 1)
            currSum -= candidates[i]
            curr.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            dfs(i)

        dfs(0)
        return res