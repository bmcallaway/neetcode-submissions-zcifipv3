class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        for num in nums[:k]:
            heapq.heappush(maxHeap, -num)
        result = []
        windowMax = -maxHeap[0]
        print("maxHeap:",maxHeap)
        result.append(windowMax)
        l = 0
        r = k

        while r < len(nums):
            heapq.heappush(maxHeap, -nums[r])
            r += 1
            maxHeap.remove(-nums[l])
            l += 1
            heapq.heapify(maxHeap)
            windowMax = -maxHeap[0]
            result.append(windowMax)
        return result


