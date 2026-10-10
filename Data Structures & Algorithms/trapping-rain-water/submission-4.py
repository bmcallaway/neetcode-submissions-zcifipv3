class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        totalVolume = 0

        while l <= r:
            minHeight = min(leftMax, rightMax)
            if leftMax <= rightMax:
                totalVolume += max(minHeight - height[l], 0)
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                totalVolume += max(minHeight - height[r], 0)
                rightMax = max(rightMax, height[r])
                r -= 1

        return totalVolume
