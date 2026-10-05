class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #1 1 2
       
        #  
        #  
        #  
        
        nums.sort()

        res, curr = [], []
        def backtrack(pos):
            nonlocal res, curr
            if pos == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[pos])
            backtrack(pos + 1)
            curr.pop()
            pos += 1
            while pos < len(nums) and nums[pos] == nums[pos-1]:
                pos += 1
            backtrack(pos)

        backtrack(0)
        return res
