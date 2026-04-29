class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = 0
        avg = 0
        count = 0
        windowSum = 0
        #1 2 3 4 5 6 7 8 9
        #l
        while r < k:
            windowSum += arr[r]
            r += 1

        avg = float(windowSum / k)
        print("windsum:",windowSum)
        print("avg:",avg)
        if avg >= threshold:
            count += 1
            print(arr[l:r+1])

        while r < len(arr):
            windowSum += arr[r]
            r += 1
            windowSum -= arr[l]
            l += 1
            avg = windowSum / k

            if avg >= threshold:
                count += 1

        return count