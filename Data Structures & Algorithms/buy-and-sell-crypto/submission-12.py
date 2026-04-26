class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxP = 0

        l = 0
        #5 1 5 6 7 1
        #l
        #  r

        r = 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l+1
            else:
                while r < len(prices) and prices[l] <= prices[r]:
                    print(l,r)
                    prof = prices[r] - prices[l]
                    maxP = max(maxP, prof)
                    r += 1
                    

        return maxP
