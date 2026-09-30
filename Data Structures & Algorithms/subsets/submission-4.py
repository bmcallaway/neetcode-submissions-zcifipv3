class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #       Add1            Add2        Add3
        #    N  A2  A3        N    A3    N    N
        #.   N  A3  N           N  
        #       N
        res = []
        currSet = []
        used = set()
        def backtrack(pos):
            nonlocal res, currSet, used
            if pos >= len(nums):
                res.append(currSet[:])
                return
            currSet.append(nums[pos])
            backtrack(pos+1)
            currSet.pop()
            backtrack(pos+1)
        backtrack(0)
        return res
#[1,2,3], [1,2], [1,3], [1], [2,3], [2],