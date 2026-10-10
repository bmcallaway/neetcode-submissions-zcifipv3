class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #           1        2         3
        #         2   3   
        #       3       2
        used = set()
        res = []
        curr = []

        def dfs(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            for num in nums:
                if num in used:
                    continue
                used.add(num)
                curr.append(num)
                dfs(i + 1)
                used.remove(curr.pop())
        
        dfs(0)
        return res
