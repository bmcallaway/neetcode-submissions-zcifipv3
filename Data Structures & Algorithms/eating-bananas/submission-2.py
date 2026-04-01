class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #1, 2, 3, 4
        
        #4, 10, 23, 25

        l = 1
        r = max(piles)

        res = r

        while l <= r:
            m = l + (r-l) // 2
            time = self.compute(piles, m)
            print("m:",m)
            print("time:", time)
            if time <= h:
                res = min(res, m)
                r = m - 1
            else: l = m + 1
        
        return res
            
            

    def compute(self, piles: List[int], mid: int) -> int:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)
        return hours
        






        