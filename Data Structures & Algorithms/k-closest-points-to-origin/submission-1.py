class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:
            distance = math.sqrt(((point[0] - 0) ** 2) + ((point[1] - 0) **2))
            heapq.heappush(pq, (distance, point))

        result = []
        for i in range(k):
            result.append(heapq.heappop(pq)[1])
        return result