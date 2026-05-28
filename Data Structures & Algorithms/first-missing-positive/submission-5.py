class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [0 0 0 0 0 0]
        # [1 1 1 1 1 1]

        # [0 0 0]
        # []

        occurences = [False] * max(nums)
        for num in nums:
            if num > 0:
                occurences[num-1] = True
            
        for i,val in enumerate(occurences):
            if not val:
                return i+1

        return len(occurences) + 1

            