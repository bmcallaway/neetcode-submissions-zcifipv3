class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        comboSum = 0
        candidates.sort()
        def dfs(i):
            nonlocal res, combo, comboSum
            if comboSum > target:
                return
            if i >= len(candidates):
                if comboSum == target:
                    res.append(combo[:])
                return
            candidate = candidates[i]
            combo.append(candidate)
            comboSum += candidate
            dfs(i+1)
            combo.pop()
            comboSum -= candidate
            i += 1
            while i < len(candidates) and candidate == candidates[i]:
                i += 1
            dfs(i)

        dfs(0)
        return res