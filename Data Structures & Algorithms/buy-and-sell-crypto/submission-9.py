class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        max_price = 0
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
                r = l + 1
            elif prices[r] > prices[l]:
                price = prices[r] - prices[l]
                max_price = max(price, max_price)
                r += 1

        return max_price