class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        #0 1 2 3 4 5 6
        buckets = [[]] * (len(nums) + 1)
        print("length:",len(buckets))
        for i in range(len(buckets)):
            #testtt
            buckets[i] = []
        
        for key, val in freq.items():
            buckets[val].append(key)
        
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for val in buckets[i]:
                res.append(val)
                k -= 1
                if k <= 0:
                    return res

        return res
