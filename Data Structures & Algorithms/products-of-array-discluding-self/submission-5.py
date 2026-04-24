class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1 1 2 8
    #   48 24 6 1
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        prefix[0] = postfix[-1] = 1

        product = 1
        for i in range(1, len(nums)):
            product = product * nums[i-1]
            prefix[i] = product
        
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product = product * nums[i+1]
            postfix[i] = product
        print(prefix,postfix)
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res