class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        used = set()
        def dfs(i):
            nonlocal res, stack, used
            if i == len(nums):
                res.append(stack[:])
                return
            for num in nums:
                if num in used:
                    continue
                stack.append(num)
                used.add(num)
                dfs(i + 1)
                used.remove(stack.pop())

        dfs(0)
        return res
    #       []
#     1     2    3
#    2 3
#   3 