class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # 1 1 2 8
       # 48 24 6 1

        pre, post = [], []
        product = 1
        pre.append(product)
        for i in range(1, len(nums)):
            product = product * nums[i-1]
            pre.append(product)
        
        product = 1
        post.append(product)
        for i in range(len(nums) - 2, -1, -1):
            product = product * nums[i + 1]
            post.append(product)

        post.reverse()
        res = []
        for i in range(len(pre)):
            res.append(pre[i] * post[i])

        return res