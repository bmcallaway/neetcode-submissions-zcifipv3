class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = [], []

        currMax = 0
        for num in height:
            prefix.append(currMax)
            currMax = max(currMax, num)

        currMax = 0
        for num in reversed(height):
            suffix.append(currMax)
            currMax = max(currMax, num)
        suffix.reverse()
        area = 0
        for i in range(len(height)):
            area += max(0, min(prefix[i], suffix[i]) - height[i])
        return area
            
        