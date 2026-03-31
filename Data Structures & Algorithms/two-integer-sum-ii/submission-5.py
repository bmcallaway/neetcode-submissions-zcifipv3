class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        ans = []
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
                continue
            elif sum < target:
                l += 1
                continue
            else:
                ans = [l+1, r+1]
                break
        return ans