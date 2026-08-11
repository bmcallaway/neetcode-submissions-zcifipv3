class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curSum = 0
        stack = []
        def backtrack(i):
            nonlocal res, curSum, stack
            if curSum >= target or i == len(nums):
                if curSum == target:
                    res.append(stack[:])
                return
            curSum += nums[i]
            stack.append(nums[i])
            backtrack(i)
            curSum -= stack.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res

#           9
#          
#         
#             
#       
#               
