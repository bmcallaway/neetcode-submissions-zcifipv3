class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        nums.sort()
        def dfs(i):
            nonlocal res, stack, freqs
            if i == len(nums):
                res.append(stack[:])
                return
            for num in freqs:
                if freqs[num] <= 0:
                    continue
                freqs[num] -= 1
                stack.append(num)
                dfs(i + 1)
                freqs[num] += 1
                stack.pop()
            

        dfs(0)
        return res