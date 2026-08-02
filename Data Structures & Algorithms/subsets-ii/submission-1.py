class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        nums.sort()
        #
        def backtrack(i: int):
            nonlocal res, stack
            if i >= len(nums):
                res.append(stack[:])
                return
            
            stack.append(nums[i])
            backtrack(i+1)
            stack.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            backtrack(i)

        backtrack(0)
        return res


