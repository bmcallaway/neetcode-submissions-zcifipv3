class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in indices:
                return [indices[diff]+1, i+1]
            indices[numbers[i]] = i
        
        return []