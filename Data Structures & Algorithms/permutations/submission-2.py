class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        used = set()

        def backtrack(i):
            nonlocal res, stack, used
            if i >= len(nums):
                res.append(stack[:])
                return
            for num in nums:
                print(num)
                if num in used:
                    print("num in used")
                    continue
                used.add(num)
                stack.append(num)
                backtrack(i+1)
                used.remove(num)
                stack.pop()
        
        backtrack(0)
        return res