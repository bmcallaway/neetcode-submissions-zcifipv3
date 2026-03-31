class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int maxP = 0;
        while(r < prices.length){
            if(prices[r]>prices[l]){
                int diff = prices[r] - prices[l];
                maxP = Math.max(diff, maxP);
            }else{
                l = r;
            }
            r++;
        }
        return maxP;
    }
}
