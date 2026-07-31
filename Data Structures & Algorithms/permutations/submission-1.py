class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        perm = []
        def backtrack(pos):
            nonlocal res, perm, used
            if pos == len(nums):
                res.append(perm[:])
                return
            for num in nums:
                if num in used:
                    continue
                used.add(num)
                perm.append(num)
                backtrack(pos + 1)
                used.remove(num)
                perm.remove(num)

        backtrack(0)
        return res