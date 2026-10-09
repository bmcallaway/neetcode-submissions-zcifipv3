class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            difference = target - num
            if difference in seen:
                return [seen[difference] + 1, i + 1]
            seen[num] = i
        
        return []