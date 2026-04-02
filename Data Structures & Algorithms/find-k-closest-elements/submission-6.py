class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l = 0
        r = len(arr) - 1 # 3

        while (r - l) >= k: #3 2
            lDiff = abs(x - arr[l]) #=4 2
            rDiff = abs(x - arr[r]) #=2 2

            if lDiff <= rDiff:
                r -= 1 #2
            else: l += 1 #1

        return arr[l:r+1] #[1:2]

