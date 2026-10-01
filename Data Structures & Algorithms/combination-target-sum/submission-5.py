class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #       2
        #  [2]
        #   2 
        #   5 6 9
        res = []
        currSum = 0
        curr = []
        def backtrack(pos):
            nonlocal res, curr, currSum
            if currSum > target or pos >= len(nums):
                return
            if currSum == target:
                res.append(curr[:])
                return
            curr.append(nums[pos])
            currSum += nums[pos]
            backtrack(pos)
            currSum -= curr.pop()
            backtrack(pos+1)

        backtrack(0)
        return res
            