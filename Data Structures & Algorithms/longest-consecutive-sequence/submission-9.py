class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        length = 0
        longest = 0
        for n in uniqueNums:
            if n+1 in uniqueNums:
                length = 2
                n += 1
                while(n+1 in uniqueNums):
                    length += 1
                    n += 1
                longest = max(length, longest)
            else:
                length = 1
        
        return max(length, longest)
        