class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #0  1  2  8
        #48 24 6  0

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        prefix[0], postfix[len(nums)-1] = 1, 1

        curSum = 1
        for i in range(1, len(nums)):
            curSum *= nums[i-1]
            prefix[i] = curSum
        
        curSum = 1
        for i in range(len(nums)-2, -1, -1):
            curSum *= nums[i+1]
            postfix[i] = curSum

        for i in range(len(nums)):
            nums[i] = prefix[i] * postfix[i]

        return nums