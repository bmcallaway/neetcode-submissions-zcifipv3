class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numsSet = set(nums)

        maxLongest = 1
        longest = 1


        for num in numsSet:
            if num-1 in numsSet:
                continue
            while num+1 in numsSet:
                longest += 1
                maxLongest = max(maxLongest, longest)
                num = num+1       
            longest = 1 
        return maxLongest
            

        