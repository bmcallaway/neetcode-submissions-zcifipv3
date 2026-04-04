class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        for number in nums:
            heapq.heappush(self.pq, -number)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, -val)
        copy = self.pq.copy()
        for i in range(self.k - 1):
            print("popping:",heapq.heappop(copy))
        popped = heapq.heappop(copy)
        print("popped:",popped)
        return -popped
        
