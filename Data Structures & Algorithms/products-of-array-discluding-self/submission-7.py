class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1 1 2 8
        #48 24 6 1

        prefix, postfix = [1] * len(nums), [1] * len(nums)
        prefix[0], postfix[len(nums)-1] = 1, 1
        curSum = 1
        for i in range(1, len(nums)):
            curSum = nums[i-1] * curSum
            prefix[i] = curSum
        curSum = 1
        for i in range(len(nums)-2, -1, -1):
            curSum = nums[i+1] * curSum
            postfix[i] = curSum
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])

        return res