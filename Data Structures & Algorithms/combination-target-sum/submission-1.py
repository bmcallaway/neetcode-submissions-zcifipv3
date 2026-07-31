class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        comboSum = 0
        def backtrack(i):
            nonlocal res, combo, comboSum
            if i >= len(nums) or comboSum > target:
                if comboSum == target:
                    res.append(combo[:])
                return
            comboSum += nums[i]
            combo.append(nums[i])
            backtrack(i)
            combo.pop()
            comboSum -= nums[i]
            backtrack(i+1)
        
        backtrack(0)

        return res
            