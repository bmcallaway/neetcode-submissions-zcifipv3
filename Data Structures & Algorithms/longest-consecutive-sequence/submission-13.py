class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()

        for num in nums:
            numSet.add(num)
        #2 20 4 10 3 5

        longest = 0
        for num in numSet:
            length = 1
            while num+1 in numSet:
                length += 1
                num = num+1
            longest = max(length, longest)


        return longest