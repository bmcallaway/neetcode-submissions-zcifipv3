class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            diff = target - nums[i];
            if(diff in indices):
                if(i < indices[diff]):
                    return [i, indices[diff]]
                else:
                    return [indices[diff], i]
            else:
                indices[nums[i]] = i
        
        return null

        