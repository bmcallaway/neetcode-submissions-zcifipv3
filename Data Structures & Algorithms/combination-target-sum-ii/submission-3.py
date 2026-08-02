class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        stack = []
        sSum = 0
        #1 2 2 4 5 6 9    

        #1 2 - 4                       
        def backtrack(i):
            nonlocal res, stack, sSum
            if sSum > target:
                return
            if i >= len(candidates):
                if sSum == target:
                    res.append(stack[:])
                return
            val = candidates[i]
            stack.append(val)
            sSum += val
            backtrack(i+1)
            stack.pop()
            sSum -= val
            i += 1
            while i < len(candidates) and val == candidates[i]:
                i += 1
            backtrack(i)

        backtrack(0)
        return res


