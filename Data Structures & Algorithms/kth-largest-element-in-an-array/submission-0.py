class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for n in nums:
            heapq.heappush(pq, -n)
        
        popped = 0
        #-5 -4 -3 -2 -1
        for i in range(k):
            popped = -heapq.heappop(pq)
        
        return popped