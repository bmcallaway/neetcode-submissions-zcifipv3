class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLongest = 0

        numSet = set(nums)

        for num in numSet:
            if num - 1 in numSet:
                continue
            longest = 1
            while num + 1 in numSet:
                longest += 1
                num += 1
            maxLongest = max(maxLongest, longest)
        
        return maxLongest
