class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = set()

        def dfs(pos):
            if pos >= len(nums):
                res.append(curr[:])
                return
            for num in nums:
                if num in used:
                    continue
                curr.append(num)
                used.add(num)
                dfs(pos + 1)
                curr.pop()
                used.remove(num)
        dfs(0)
        return res