class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
 
        res = []
        currSum = 0
        curr = []
        candidates.sort()
        def backtrack(pos):
            nonlocal res, curr, currSum
            if currSum > target or pos >= len(candidates):
                if currSum == target:
                    res.append(curr[:])
                return
            curr.append(candidates[pos])
            currSum += candidates[pos]
            pos += 1
            backtrack(pos)
            currSum -= curr.pop()
            while pos < len(candidates) and candidates[pos] == candidates[pos-1]:
                pos += 1
            backtrack(pos)

        backtrack(0)
        return res
            