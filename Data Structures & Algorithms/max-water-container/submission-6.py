class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxVolume = 0
        while l < r:
            volume = (r - l) * min(heights[l], heights[r])
            maxVolume = max(maxVolume, volume)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        
        return maxVolume
