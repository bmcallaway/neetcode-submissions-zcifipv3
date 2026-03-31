class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxvolume = 0
        while l < r:
            shortbar = min(heights[l], heights[r])
            volume = shortbar * (r-l)
            maxvolume = max(maxvolume, volume)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return maxvolume

        