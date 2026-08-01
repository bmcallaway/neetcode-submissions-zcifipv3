class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        stackSum = 0
        def backtrack(i):
            nonlocal stackSum, res, stack
            if i >= len(nums) or stackSum > target:
                return
            if stackSum == target:
                res.append(stack[:])
                return
            # 2 2 2 2
            stackSum += nums[i]
            stack.append(nums[i])
            backtrack(i)
            stack.pop()
            stackSum -= nums[i]
            backtrack(i+1)

        backtrack(0)

        return res
