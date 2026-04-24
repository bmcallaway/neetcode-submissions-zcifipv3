class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        uniqueNums = set(nums)

        for num in uniqueNums:
            if num+1 in uniqueNums:
                length = 2
                val = num + 1
                while val + 1 in uniqueNums:
                    length += 1
                    val = val + 1
            else: length = 1
            longest = max(longest, length)

        return longest