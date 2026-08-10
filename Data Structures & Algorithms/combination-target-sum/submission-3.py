class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #       2
        #      2 5
        res = []
        currSum = 0
        stack = []

        def backtrack(pos):
            nonlocal res, currSum, stack
            if currSum == target:
                res.append(stack[:])
                return
            elif currSum > target or pos == len(nums):
                return
            currSum += nums[pos]
            stack.append(nums[pos])
            backtrack(pos)
            currSum -= stack.pop()
            backtrack(pos+1)

        backtrack(0)
        return res

            
                