class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1 - 1
        #2 - 2
        #3 - 3

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])
        
        for key,val in freq.items():
            buckets[val].append(key)

        result = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
            
