class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = k - 1

        while r < len(arr)-1:
            if abs(x - arr[r+1]) < abs(x-arr[l]) or arr[r+1] == arr[l]:
                l += 1
                r += 1
            else: break
            
        res = []
        for i in range(l, r+1):
            res.append(arr[i])

        return res