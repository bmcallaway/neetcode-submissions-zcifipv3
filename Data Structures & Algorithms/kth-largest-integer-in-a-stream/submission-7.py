class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        for number in nums:
            heapq.heappush(self.pq, -number)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, -val)
        copy = self.pq.copy()
        popped = 0
        for i in range(self.k):
            popped = heapq.heappop(copy)
        return -popped
        
