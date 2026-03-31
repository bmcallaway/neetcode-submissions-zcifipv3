class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3
        for n in nums:
            buckets[n] += 1
        i = 0
        for _ in range(buckets[0]):
            print("test 0")
            nums[i] = 0
            i += 1
        for _ in range(buckets[1]):
            print("test 1")
            nums[i] = 1
            i += 1
        for _ in range(buckets[2]):
            print("test 2")
            nums[i] = 2
            i += 1