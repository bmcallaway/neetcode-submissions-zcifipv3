class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1 = 1
        #2 = 2
        #3 = 3

        #[] [1] [2] [3]

        #.           i
        res = []
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for key, val in freqs.items():
            print(key, val)
            print(buckets[0])
            print(buckets[val])
            buckets[val].append(key)
        count = 0
        for i in range(len(buckets)-1, -1, -1):
            print(i, buckets[i])
            for element in buckets[i]:
                res.append(element)
                count += 1
                if count >= k:
                    return res

        return []
