class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)

        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = nums[i] * pre[i-1]
        post[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            post[i] = nums[i] * post[i+1]

        print("pre: ", pre)
        print("post: ", post)
        nums[0] = 1 * post[1];
        nums[len(nums)-1] = 1 * pre[len(nums)-2]

        for i in range(1, len(nums)-1):
            nums[i] = pre[i-1] * post[i+1]

        return nums
