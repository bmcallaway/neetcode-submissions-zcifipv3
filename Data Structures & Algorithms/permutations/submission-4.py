# 1, 2, 3
#   2, 3
#    3

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = set()
        def backtrack(pos):
            nonlocal res, used
            if pos >= len(nums):
                res.append(curr[:])
                return
            for num in nums:
                if num in used:
                    continue
                curr.append(num)
                used.add(num)
                backtrack(pos+1)
                used.remove(num)
                curr.remove(num)

        backtrack(0)
        return res