class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for weight in stones:
            heapq.heappush(pq, -weight)
        
        while len(pq) > 1:
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(pq, -(y-x))
        if len(pq) == 0: return 0
        return -pq[0]