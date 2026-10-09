class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        buckets = []

        for _ in range(len(nums) + 1):
            buckets.append([])
        
        for key, val in freqs.items():
            buckets[val].append(key)
        
        res = []
        idx = 0
        for i in range(len(nums), 0, -1):
            for val in buckets[i]:
                res.append(val)
                idx += 1
                if idx >= k:
                    return res

        return res
